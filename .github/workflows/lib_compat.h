// This header forces the use of a particular version of glibc symbols.
// This can make the resulting binary portable to systems with older glibcs.
//
// It must be included in each TU, with CFLAGS="-include glibc_compat.h" etc.
//
// We only list symbols known to be used. This is paired with a test enforcing
// the max glibc symbol version. If the test fails, the list should be extended.
// Find the old alternatives version to target with e.g.:
//   objdump -T /lib/x86_64-linux-gnu/lib{c,m,pthread,rt}.so.* | grep "\bexpf\b"

#define FORCE_SYMBOL_VERSION(sym, version) \
  __asm__(".symver " #sym "," #sym "@" #version)

FORCE_SYMBOL_VERSION(exp2, GLIBC_2.2.5);
FORCE_SYMBOL_VERSION(expf, GLIBC_2.2.5);
FORCE_SYMBOL_VERSION(log, GLIBC_2.2.5);
FORCE_SYMBOL_VERSION(log2, GLIBC_2.2.5);
FORCE_SYMBOL_VERSION(pow, GLIBC_2.2.5);
FORCE_SYMBOL_VERSION(exp, GLIBC_2.2.5);

#undef FORCE_SYMBOL_VERSION
