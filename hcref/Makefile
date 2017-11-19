#!/bin/bash
######
# Makefile for 'hcref'
######

CC=cc
CCOPTS=
CFILES=error.c globals.c hcref.c list.c scanner.c utils.c
HFILES=error.h globals.h hcref.h list.h portable.h scanner.h utils.h 

hcref:	$(CFILES) $(HFILES) Makefile
	$(CC) -o hcref $(CCOPTS) $(CFILES)

clean:
	-rm -Rf *.o hcref hcref.out

backup:
	cp -p $(CFILES) backup.dir
	cp -p $(HFILES) backup.dir

test:	hcref
	-rm -Rf hcref.out
	hcref -n -k -# -ohcref.out $(CFILES) $(HFILES)

dos2unix:
	dos2unix error.c error.c
	dos2unix error.h error.h
	dos2unix globals.c globals.c
	dos2unix globals.h globals.h
	dos2unix hcref.c  hcref.c
	dos2unix hcref.h hcref.h
	dos2unix list.c list.c
	dos2unix list.h list.h
	dos2unix portable.h portable.h
	dos2unix scanner.c scanner.c
	dos2unix scanner.h scanner.h
	dos2unix utils.c utils.c
	dos2unix utils.h utils.h
