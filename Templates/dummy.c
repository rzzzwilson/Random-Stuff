/******************************************************************************\
 *                                   dummy                                    *
 *                                  =======                                   *
 *                                                                            *
 *  This program is a simple 'boiler-plate' program used to ease starting     *
 *  programs of this type, ie, UNIX filters.  It is called:                   *
 *                                                                            *
 *      dummy [ <filein> [ <fileout> ] ]                                      *
 *                                                                            *
 *  where <filein>   is an input filename                                     *
 *        <fileout>  is an output filename                                    *
 *                                                                            *
 *  If no output filename is supplied then 'stdout' is used.                  *
 *  If no input filename is supplied then 'stdin' is used.                    *
 *                                                                            *
 *  This sample program simply copies input to output.                        *
 *                                                                            *
\******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <errno.h>

#ifdef __BORLANDC__
#   include <stdarg.h>
#else
#   include <sys/varargs.h>
#endif

/******
 * Local constants.
 ******/

#define PROGNAME        "dummy"

#define EXIT_OK         0
#define EXIT_ERROR      1


/******
 * Globals
 ******/

static char *ProgName = NULL;
static char *infname = "stdin";
static char *outfname = "stdout";


/******************************************************************************
       Name : dummy()
Description : Production function for the "dummy" program.
 Parameters : ?
    Returns : ?
   Comments :
 ******************************************************************************/
int
dummy(FILE *in, FILE *out)
{
    int ch;

    errno = 0;

    while ((ch = getc(in)) != EOF)
    {
        if (fprintf(out, "%c", ch) < 0)
            error("Error writing to output file '%s': %s",
                  outfname, strerror(errno)
                 );
    }

    if (errno != 0)
        error("Error reading from input '%s': %s",
              infname, strerror(errno)
             );

    return 0;
}


/******************************************************************************
       Name : error()
Description : printf()-style error routine.
 Parameters : like printf()
    Returns : Doesn't, calls exit().
   Comments :
 ******************************************************************************/
void
error(char *fmt, ...)
{
    va_list ap;

    va_start(ap, fmt);
    vfprintf(stderr, fmt, ap);
    fprintf(stderr, "\n");
    va_end(ap);

    exit(EXIT_ERROR);
}


/******************************************************************************
       Name : usage()
Description : Function to provide much needed help to user.
 Parameters :
    Returns : Doesn't, calls error().
   Comments : Expects global "ProgName" to point to program name.
 ******************************************************************************/
void
usage(void)
{
    error("usage: %s [ <input> [ <output ] ]", ProgName);
}


/******************************************************************************
       Name : main()
Description :
 Parameters :
    Returns :
   Comments :
 ******************************************************************************/
int
main(int argc, char *argv[])
{
    FILE *in = stdin;
    FILE *out = stdout;

/******
 * Initialize globals
 ******/

    ProgName = strrchr(argv[0], '\\');
    if (ProgName == NULL)
        ProgName = PROGNAME;
    else
        ++ProgName;

/******
 * Now analyze params.
 ******/

    switch (argc)
    {
        case 3:
            outfname = argv[2];
            out = fopen(outfname, "w");
            if (out == NULL)
            error("Error opening '%s' for output: %s",
                  outfname, strerror(errno)
                 );
            /* FALLTHROUGH */
        case 2:
            infname = argv[1];
            in = fopen(infname, "r");
            if (in == NULL)
            {
                if (argc == 3)
                {
                    fclose(out);
                    unlink(outfname);
                }
                error("Error opening '%s' for input: %s",
                      infname, strerror(errno)
                     );
            }
            /* FALLTHROUGH */
        case 1:
            break;

        default:
            usage();
    }

/******
 * Now call the production routine - dummy()
 ******/

    dummy(in, out);

/******
 * Close down
 ******/

    if (in != stdin)
        if (fclose(in) != 0)
            error("Error closing input file '%s': %s",
                  infname, strerror(errno)
                 );
    if (out != stdout)
        if (fclose(out) != 0)
            error("Error closing output file '%s': %s",
                  outfname, strerror(errno)
                 );

    return EXIT_OK;                     /* to keep compiler happy! */
}
