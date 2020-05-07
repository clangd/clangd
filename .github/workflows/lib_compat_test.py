#!/usr/bin/env python3

# Verifies a binary uses only dynamic symbols from whitelisted library versions.
# Prints the disallowed symbols and their versions on failure.
# Usage: lib_compat_test.py bin/clangd --lib=GLIBC_2.18

import argparse
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument("binary")
parser.add_argument(
    "--lib",
    action="append",
    default=[],
    help="Whitelist a library, e.g. GLIBC_2.18 or GLIBC",
)
parser.add_argument(
    "--sym", action="append", default=[], help="Whitelist a symbol, e.g. crc32"
)
args = parser.parse_args()

# Parses GLIBC_2.3 into ("GLIBC", [2,3])
# Parses GLIBC into ("GLIBC", None)
def parse_version(version):
    parts = version.rsplit("_", 1)
    if len(parts) == 1:
        return (version, None)
    try:
        return (parts[0], [int(p) for p in parts[1].split(".")])
    except ValueError:
        return (version, None)


lib_versions = dict([parse_version(v) for v in args.lib])

# Determines whether all symbols with version 'lib' are acceptable.
# A versioned library is name_x.y.z by convention.
def accept_lib(lib):
    (lib, ver) = parse_version(lib)
    if not lib in lib_versions:  # Non-whitelisted library.
        return False
    if lib_versions[lib] is None:  # Unrestricted version
        return True
    if ver is None:  # Lib has non-numeric version, library restricts version.
        return False
    return ver <= lib_versions[lib]


# Determines whether an optionally-versioned symbol is acceptable.
# A versioned symbol is symbol@version as output by nm.
def accept_symbol(sym):
    if sym in args.sym:
        return True
    split = sym.split("@", 1)
    return (split[0] in args.sym) or (len(split) == 2 and accept_lib(split[1]))


# Run nm to find the undefined symbols, and check whether each is acceptable.
nm = subprocess.run(
    ["nm", "-uD", "--with-symbol-version", args.binary],
    stdout=subprocess.PIPE,
    universal_newlines=True,
)
nm.check_returncode()
status = 0
for line in nm.stdout.splitlines():
    # line = "       U foo@GLIBC_2.3"
    parts = line.split()
    if len(parts) != 2:
        print("Unparseable nm output: ", line, file=sys.stderr)
        status = 2
        continue
    if parts[0] == "w":  # Weak-undefined symbol, not actually required.
        continue
    if not accept_symbol(parts[1]):
        print(parts[1])
        status = 1
if status == 1:
    print(
        "Binary depends on disallowed symbols above. Use some combination of:\n"
        " - relax the whitelist by adding --lib and --sym flags to this test\n"
        " - force older symbol versions by updating lib_compat.h\n"
        " - avoid dynamic dependencies by changing CMake configuration\n"
        " - remove bad dependencies from the code",
        file=sys.stderr,
    )
sys.exit(status)
