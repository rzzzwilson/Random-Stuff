#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MCDEBUG
#include "memcheck.h"

void
callback(char *fmt, ...)
{
   va_list args;

   va_start(args, fmt);
   vfprintf(stdout, fmt, args);
   va_end(args);
}


int
main(int argc, char *argv[])
{
    char *new;
    long i;
    long iter = 1000000L;

    if (argc > 1)
        iter = atol(argv[1]);

    MCinit(0, callback);
#ifdef JUNK
    MCinit(0, NULL);
#endif

/* allocate and free block */

    new = malloc(10);
    strcpy(new, "10 freed");
    free(new);

/* block of size 1 will be left allocated */

    new = malloc(1);

/* block of size 2 will have underrun and left allocated */

    new = malloc(2);
    *(new - 1) = 'A';
    
/* block of size 3 will have overrun and left allocated */

    new = malloc(3);
    *(new + 4) = 'B';

/* block of size 4 will have overrun and underrun and left allocated */

    new = malloc(4);
    *(new - 2) = 'C';
    *(new + 6) = 'D';

/* allocate and free block */

    new = malloc(11);
    strcpy(new, "11 freed");
    free(new);

/* block of size 5 will have underrun */

    new = malloc(5);
    *(new - 1) = 'A';
    free(new);
    
/* block of size 6 will have overrun */

    new = malloc(6);
    *(new + 9) = 'B';
    free(new);
    
/* block of size 7 will have overrun and underrun */

    new = malloc(7);
    *(new - 2) = 'C';
    *(new + 10) = 'D';
    free(new);

/* allocate and free block */

    new = malloc(12);
    strcpy(new, "12 freed");
    free(new);

/* realloced block of size 9 will be left allocated */

    new = malloc(8);
    new = realloc(new, 9);

/* realloced block of size 11 will have underrun and left allocated */

    new = malloc(10);
    new = realloc(new, 11);
    *(new - 1) = 'A';
    
/* realloced block of size 13 will have overrun and left allocated */

    new = malloc(12);
    new = realloc(new, 13);
    *(new + 14) = 'B';
    
/* realloced block of size 15 will have overrun and underrun and left allocated */

    new = malloc(14);
    new = realloc(new, 15);
    *(new - 2) = 'C';
    *(new + 16) = 'D';

/* realloced block of size 17 will have underrun */

    new = malloc(16);
    new = realloc(new, 17);
    *(new - 1) = 'A';
    free(new);
    
/* realloced block of size 19 will have overrun */

    new = malloc(18);
    new = realloc(new, 19);
    *(new + 20) = 'B';
    free(new);
    
/* realloced block of size 21 will have overrun and underrun */

    new = malloc(20);
    new = realloc(new, 21);
    *(new - 2) = 'C';
    *(new + 22) = 'D';
    free(new);

/* block of size 22 will be underrun and then realloced */

    new = malloc(22);
    *(new - 1) = 'A';
    new = realloc(new, 23);
    free(new);
    
/* block of size 24 will be overrun and then realloced */

    new = malloc(24);
    *(new + 25) = 'A';
    new = realloc(new, 25);
    free(new);
    
/* block of size 26 will be over and underrun and then realloced */

    new = malloc(26);
    *(new - 1) = 'A';
    *(new + 27) = 'A';
    new = realloc(new, 27);
    free(new);

/* allocate and free block */

    new = malloc(13);
    strcpy(new, "13 freed");
    free(new);

/* block of size 28 will be freed and then changed */

    new = malloc(28);
    free(new);
    *(new + 2) = 'E';
    
/* free block twice */

    new = malloc(29);
    free(new);
    free(new);

/* free unallocated block */

    free((void *) 1);

/* allocate and free a large number of blocks */
    for (i = 0; i < iter; ++i)
    {
        new = malloc(30);
        if (new == NULL)
        {
            fprintf(stderr, "Out of memory!?\n");
            exit(10);
        }
        free(new);
    }

    return 0;
}
