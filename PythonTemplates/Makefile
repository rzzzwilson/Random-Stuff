#
# Test the template programs
#

#GCCOPTS=-Wall -Wextra -ansi -pedantic
GCCOPTS=-Wall -Wextra -std=c89 -pedantic -Wmissing-prototypes -Wstrict-prototypes -Wold-style-definition

test:
	template_cli
	python template_cli.py
	python template_wxpython.py

template_cli:	template_cli.c Makefile
	gcc $(GCCOPTS) -o template_cli template_cli.c

clean:
	rm -f template_cli
