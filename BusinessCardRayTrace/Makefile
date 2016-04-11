#
# Build the business crad ray tracers, and run them
#

test:	card
	card >card.ppm

test_sane:	card_sane Makefile
	card_sane >card_sane.ppm

card:	card.cpp Makefile
	c++ -o card card.cpp

card_sane:	card_sane.cpp Makefile
	c++ -o card_sane card_sane.cpp

python:
	python rt.py > python.ppm

clean:
	rm -f *.o card.ppm python.ppm card card_sane
