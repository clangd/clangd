# Convince find_package() to link against libz.a instead of libz.so.
# The default is ".so;.a", meaning dynamic libraries are preferred.
set(CMAKE_FIND_LIBRARY_SUFFIXES ".a")
