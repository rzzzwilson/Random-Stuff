#
# Build all C executables
#

#GCC_OPTS="-std=c99 -Wall -pedantic"
GCC_OPTS="-pedantic"

clean:
	rm -Rf *.pyc *.o

all:		write_PPM write_PPM2 write_PPM3 write_PPM4

write_PPM:  write_PPM.c Makefile
	gcc $(GCC_OPTS) -o $@  $<

write_PPM2: write_PPM2.c Makefile vec3.h
	gcc $(GCC_OPTS) -o $@  $<

write_PPM3: write_PPM3.c Makefile vec3.h
	gcc $(GCC_OPTS) -o $@  $<

write_PPM4: write_PPM4.c Makefile vec3.h
	gcc $(GCC_OPTS) -o $@  $<
