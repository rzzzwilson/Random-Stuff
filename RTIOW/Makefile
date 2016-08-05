#
# Build all C executables
#

#GCC_OPTS="-std=c99 -Wall -pedantic"
GCC_OPTS="-pedantic"

all:		write_PPM write_PPM2

write_PPM:  write_PPM.c Makefile
	gcc $(GCC_OPTS) -o $@  $<

write_PPM2: write_PPM2.c Makefile vec3.h
	gcc $(GCC_OPTS) -o $@  $<
