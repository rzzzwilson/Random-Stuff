#include <ctype.h>
#include <stdio.h>
#include <getopt.h>

void usage(void);	/* required if -Wmissing-prototypes used */


int
the_business(int aflag, int cflag, char *cvalue)
{
    printf("the_business: aflag=%d, bflag=%d, cvalue=%s\n",
           aflag, bflag, cvalue);
    return 0;
}

void
usage(void)
{
    printf("\nExample C program.\n\n");
    printf("Usage: template_cli [-a] -[b] [-c <value>] [-h]\n\n");
}

int
main(int argc, char *argv[])
{
    int aflag = 0;
    int bflag = 0;
    char *cvalue = NULL;
    int index;
    int c;

    opterr = 0;
    while ((c = getopt(argc, argv, "abc:h")) != -1)
    {
        switch (c)
        {
            case 'a':
                aflag = 1;
                break;
            case 'b':
                bflag = 1;
                break;
            case 'c':
                cvalue = optarg;
                break;
	    case 'h':
		usage();
		return 0;
            case '?':
                if (optopt == 'c')
                    fprintf(stderr, "Option -%c requires an argument.\n", optopt);
                else if (isprint(optopt))
                    fprintf(stderr, "Unknown option '-%c'.\n", optopt);
                else
                    fprintf(stderr, "Unknown option character '\\x%x'.\n", optopt);
                return 1;
        }
    }

    printf("aflag=%d, bflag=%d, cvalue=%s\n", aflag, bflag, cvalue);

    for (index = optind; index < argc; index++)
        printf("Non-option argument %s\n", argv[index]);

    return the_business(aflag, bflag, cvalue);
}
