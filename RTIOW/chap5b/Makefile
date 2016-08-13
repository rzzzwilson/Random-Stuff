#
# Build the C executable.
# Run the two programs and compare outputs.
#

GCC_OPTS="-pedantic"

main:	main.c Makefile
	gcc $(GCC_OPTS) -o $@  $<

run:    main
	./main >main.ppm
	python main.py >main.py.ppm
	diff main.ppm main.py.ppm

clean:
	rm -Rf *.pyc *.o *.ppm main

