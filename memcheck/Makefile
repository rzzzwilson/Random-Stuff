################################################################################
# Makefile for 'memcheck'.
################################################################################

CCOPTS=-g -Wall -std=c99 -pedantic-errors -Wstrict-prototypes

all:		memcheck

memcheck:	memcheck.o test.o Makefile
		cc -o memcheck test.o memcheck.o

memcheck.o:	memcheck.c memcheck.h Makefile
		$(CC) -c $(CCOPTS) memcheck.c

test.o:		test.c memcheck.h Makefile
		$(CC) -c $(CCOPTS) test.c

test:		memcheck
		@echo "1000000" 1>&2
		time ./memcheck 1000000
		@echo "2000000" 1>&2
		time ./memcheck 2000000
		@echo "3000000" 1>&2
		time ./memcheck 3000000
		@echo "4000000" 1>&2
		time ./memcheck 4000000
		@echo "5000000" 1>&2
		time ./memcheck 5000000
		@echo "6000000" 1>&2
		time ./memcheck 6000000
		@echo "7000000" 1>&2
		time ./memcheck 7000000
#		@echo "8000000" 1>&2
#		time ./memcheck 8000000

clean:		
		rm -f *.o memcheck core *.tar *~

tar:
		tar cf memcheck.tar Makefile test.c memcheck.c memcheck.h
