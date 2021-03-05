#!/usr/bin/env python
import os, sys, json

EXTS = ('.c','.C','.cpp','.cc','.cxx','.m','.mm'
        '.h','.H','.hpp','.hh','.hxx')

input = sys.argv[1] if len(sys.argv) > 1 else 'compile_flags.txt'
driver = sys.argv[2] if len(sys.argv) > 2 else 'clang'
with open(input) as f:
    flags = [line.strip() for line in f]

dir = os.path.dirname(os.path.abspath(input))

entries = []

for root, dirs, files in os.walk(dir):
    for file in files:
        ext = os.path.splitext(file)[1]
        if ext in EXTS:
            entries.append({
                'directory': dir,
                'file': os.path.join(dir, file),
                'arguments': [driver] + flags + [os.path.join(dir, file)]})

with open(os.path.join(dir, 'compile_commands.json'), 'w') as file:
    json.dump(entries, file, indent=2)

