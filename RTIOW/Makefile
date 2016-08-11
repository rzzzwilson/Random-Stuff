#
# Build all C executables
#

#GCC_OPTS="-std=c99 -Wall -pedantic"
GCC_OPTS="-pedantic"
TARGETS=write_PPM write_PPM2 write_PPM3 write_PPM4 write_PPM5 write_PPM5b

clean:
	rm -Rf *.pyc *.o $(TARGETS)

all:    $(TARGETS)

write_PPM:  write_PPM.c Makefile
	gcc $(GCC_OPTS) -o $@  $<

write_PPM2: write_PPM2.c Makefile vec3.h
	gcc $(GCC_OPTS) -o $@  $<

write_PPM3: write_PPM3.c Makefile vec3.h ray.h
	gcc $(GCC_OPTS) -o $@  $<

write_PPM4: write_PPM4.c Makefile vec3.h ray.h
	gcc $(GCC_OPTS) -o $@  $<

write_PPM5: write_PPM5.c Makefile vec3.h ray.h
	gcc $(GCC_OPTS) -o $@  $<

write_PPM5b: write_PPM5b.c Makefile vec3.h ray.h hitable.h hitable_list.h
	gcc $(GCC_OPTS) -o $@  $<
