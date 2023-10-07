---
name: Bug report
about: A problem encountered using clangd
title: ''
labels: ''
assignees: ''

---

Please describe the problem.
For hints on what information is helpful, see: https://clangd.llvm.org/troubleshooting.html

If you can, provide a minimal chunk of code that shows the problem (either inline, or attach it if larger).

**Logs**

Please attach the clangd stderr log if you can. (Usually available from the editor)
If possible, run with `--log=verbose` - note that the logs will include the contents of open files!
If this is a crash, try to put `llvm-symbolizer` on your PATH per the troubleshooting instructions.
(If you're using Windows, place the associated PDB file (debug symbols) in the same directory as
clangd.exe and rerun again. For official releases, download symbols from the
[release page](https://github.com/clangd/clangd/releases).)

**System information**

Output of `clangd --version`:

Editor/LSP plugin:

Operating system:
