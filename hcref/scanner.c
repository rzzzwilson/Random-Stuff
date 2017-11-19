/******************************************************************************\
 *                               S C A N N E R . C                            *
 *                              ===================                           *
 *                                                                            *
 *      This file contains routines to read from a code file, return tokens   *
 *      to the caller and also emit the scanned text to an HTML file.         *
 *                                                                            *
 *      This file, without doubt, contains the oldest code of hcref, and      *
 *      therefore is the worst code in the program.  This file should be      *
 *      totally replaced with a lex/yacc scanner at the first chance!         *
 *                                                                            *
 *      The scanner must do two things:                                       *
 *              1. Find and return tokens to the caller.                      *
 *              2. Generate an HTML version of the scanned file in the        *
 *                 directory the caller wants.                                *
 *                                                                            *
 *      To this end, the scan_open() routine needs to know the directory      *
 *      that will contain the hcref listing files as the tokens in the        *
 *      HTML output file will link back to those listing files.               *
 *                                                                            *
 *      So, the HTML files will contain:                                      *
 *              1. The usual HTML header stuff, and "<pre>" at the top        *
 *              2. <a name="linexxx"> ... </a> around each line               *
 *              3. <a href="hcrefdir/hcref_t#token> ... </a> around           *
 *                 each token in the input file                               *
 *              4. replace each sensitive character (eg, '<') in the input    *
 *                 file with the &xx; escaped form                            *
 *              5. </pre> and the usual footer stuff                          *
 *                                                                            *
 *      The hcref listing files will be broken into files with the name       *
 *      "hcref_x.html" where the 'x' is the first character of the tokens     *
 *      in that file.  So there will be files "hcref_a.html", "hcref_b.html"  *
 *      and so on in the hcrefdir directory.  If numbers/#tokens are included *
 *      in the listing output, there will be files with names "hcref_0.html", *
 *      "hcref_1.html" and "hcref_.html".  The '#' character is dropped in    *
 *      filenames and token references as it confuses browsers.               *
 *                                                                            *
\******************************************************************************/

#include "portable.h"
#ifdef __BORLANDC__
#   include <dir.h>
#else
   #include <sys/types.h>
#   include <sys/stat.h>
#endif

#include "scanner.h"
#include "error.h"
#include "globals.h"
#include "utils.h"

/******
 * Local macro and constant definitions
 ******/

#define ishexdigit(a)   (('A' <= toupper(a)) && (toupper(a) <= 'F'))

/******
 * Static variables
 ******/

static char in_file[FILENAME_LEN];
static char out_file[FILENAME_LEN];
static FILE *in;
static FILE *out;
static char *codedir;

static char buffer[1024];
static char *tfore;
static char *taft;

static bool got_include = FALSE;

static void flush(void);

static char tok_buff[TOKBUFF_LEN];
static int  line_count;                    /* line counter in input file(s) */
static int  braces;
static int  parentheses;

static char prefix[FILENAME_LEN];

static bool firstnonspace;

/******
 * Function prototypes.
 ******/

static bool newline(void);


/*******************************************************************************
       Name :
Description :
 Parameters :
    Returns :
   Comments :                                                                   
*******************************************************************************/
static int
escape_ch(void)
{
    if (*tfore == '\\')
        ++tfore;

    if (*tfore == '\n')
    {
        flush();
        if (!newline())
            return (int) EOF;
    }
    
    return (int) NULL;
}


/*******************************************************************************
       Name : scan_open()
Description : Prepare the scan routines.
 Parameters : infile  - name of the file to scan
            : outfile - name of the output HTML file
            : cdir    - name of directory to hold HTML code
    Returns :
   Comments :
*******************************************************************************/
void
scan_open(char *infile, char *outfile, char *cdir)
{
    char diroutfile[FILENAME_LEN];
    char buff[FILENAME_LEN];
    char *chptr;

    sprintf(diroutfile, "%s%c%s.html", cdir, dirdelim, outfile);

    strcpy(in_file, infile);
    strcpy(out_file, outfile);
    codedir = cdir;

    in = fopen(infile, "r");
    if (in == NULL)
    {
        error("Can't open file '%s' for reading: %s\n",
                  infile, strerror(errno));
        exit(RET_ERROR);
    }

    if (!newline())
        error("Error reading file '%s': %s\n", infile, strerror(errno));

    line_count = 1;

/******
 * Create the directories we need.
 ******/

    chptr = strcpy(buff, diroutfile);
    while ((chptr = strchr(chptr, dirdelim)) != NULL)
    {
        *chptr = '\0';

        if (strlen(buff) != 0 && strcmp(buff, cdir) != 0)
        {
#ifdef __BORLANDC__
            if (mkdir(buff) == -1)
            {
                if (errno != 5)
                    error("Error creating directory '%s': %s",
                          buff, strerror(errno));
            }
#else
            if (mkdir(buff, S_IRWXU + S_IRWXG + S_IRWXO) == -1)
            {
                if (errno != 17)
                error("Error creating directory '%s': %s",
                      buff, strerror(errno));
            }
#endif
        }

        *chptr = dirdelim;
        ++chptr;
    }

/******
 * Now open the output file.
 ******/

    out = fopen(diroutfile, "w");
    if (out == NULL)
        error("Can't open file '%s' for writing: %s\n",
              diroutfile, strerror(errno));

    sprintf(buff, "file: %s", infile);
    HTML_bodyheader(out, buff);
    fprintf(out, "<pre>\n");
    fprintf(out, "<a name=\"line1\">");

/******
 * Generate the prefix used for links from HTML file back to hcref listings.
 ******/

    strcpy(prefix, "");
    for (chptr = outfile;
         (chptr = strchr(chptr, dirdelim)) != NULL;
          ++chptr)
    {
        sprintf(prefix + strlen(prefix), "..%c", dirdelim);
    }
}


/*******************************************************************************
       Name : newline()
Description : Get the next line from the input file.
 Parameters :
    Returns :
   Comments :
*******************************************************************************/
static bool
newline(void)
{
    memset(buffer, '\n', sizeof(buffer));

    if (fgets(buffer, sizeof(buffer), in) == NULL)
        return FALSE;
    ++line_count;
    tfore = taft = buffer;

    firstnonspace = TRUE;
    got_include = FALSE;

    return TRUE;
}


/*******************************************************************************
       Name :
Description :
 Parameters :
    Returns :
   Comments :
*******************************************************************************/
char *
scan_token(int *lnum, bool *defn)
{
    char  prev_ch;
    char  *tbuff_ptr;
    static bool bump_tfore = FALSE;

    *defn = FALSE;

    if (bump_tfore)
    {
        ++tfore;
        bump_tfore = FALSE;
    }

    for (;;)
    {
        flush();

        switch (*tfore)
        {
            case ' ':
            case '\t':
                ++tfore;
                continue;
            case '\n':
                ++tfore;
                flush();
                fprintf(out, "</a>");
                if (!newline())
                {
                    return NULL;
                }
                fprintf(out, "<a name=\"line%d\">", line_count);
                continue;
            case '{':
                firstnonspace = FALSE;
                ++braces;
                ++tfore;
                continue;
            case '}':
                firstnonspace = FALSE;
                --braces;
                ++tfore;
                continue;
            case '(':
                firstnonspace = FALSE;
                ++parentheses;
                ++tfore;
                continue;
            case ')':
                firstnonspace = FALSE;
                --parentheses;
                ++tfore;
                continue;
            case '_':
            case 'a': case 'b': case 'c': case 'd': case 'e':
            case 'f': case 'g': case 'h': case 'i': case 'j':
            case 'k': case 'l': case 'm': case 'n': case 'o':
            case 'p': case 'q': case 'r': case 's': case 't':
            case 'u': case 'v': case 'w': case 'x': case 'y': case 'z':
            case 'A': case 'B': case 'C': case 'D': case 'E':
            case 'F': case 'G': case 'H': case 'I': case 'J':
            case 'K': case 'L': case 'M': case 'N': case 'O':
            case 'P': case 'Q': case 'R': case 'S': case 'T':
            case 'U': case 'V': case 'W': case 'X': case 'Y': case 'Z':
                firstnonspace = FALSE;
                flush();
                tbuff_ptr = tok_buff;
                while ((isalpha(*tfore) || isdigit(*tfore) || (*tfore == '_')))
                    *tbuff_ptr++ = *tfore++;
                *tbuff_ptr = '\0';
                *lnum = line_count;
                *defn = ((parentheses == 0) && (braces == 0));
                return tok_buff;
            case '\'':
                firstnonspace = FALSE;
                for (;;)
                {
                    if (*++tfore == '\'')
                        break;
                    if (escape_ch() == EOF)
                    {
                        return NULL;
                    }
                }
                ++tfore;
                continue;
            case '/':
                firstnonspace = FALSE;
                ++tfore;
                if (*tfore == '/')
                {
                    do
                        ++tfore;
                    while (*tfore != '\n');
                }
                else if (*tfore == '*')
                {
                    ++tfore;
                    for (;;)
                    {
                        while (*tfore != '*')
                        {
                            if (*tfore == '\n')
                            {
                                ++tfore;
                                flush();
                                fprintf(out, "</a>");
                                if (!newline())
                                {
                                    return NULL;
                                }
                                fprintf(out, "<a name=\"line%d\">", line_count);
                            }
                            else
                                ++tfore;
                        }
                        ++tfore;
                        if (*tfore == '/')
                            break;
                    }
                }
                ++tfore;
                continue;
            case '0': case '1': case '2': case '3': case '4':
            case '5': case '6': case '7': case '8': case '9':
                firstnonspace = FALSE;
                prev_ch = *tfore;
                tbuff_ptr = tok_buff;
                *tbuff_ptr++ = *tfore;
                ++tfore;
                if ((toupper(*tfore) == 'X') && (prev_ch == '0'))
                {
                    *tbuff_ptr++ = *tfore;
                    ++tfore;
                }
                while (isdigit(*tfore) || ishexdigit(*tfore))
                {
                    *tbuff_ptr++ = *tfore++;
                    if (*tfore == '\n')
                        break;
                }
                *tbuff_ptr = '\0';
                if (numbertokens == TRUE)
                {
                    *lnum = line_count;
                    *defn = ((parentheses == 0) && (braces == 0));
                    return tok_buff;
                }
                continue;
            case '#':
                if (firstnonspace)
                {
                    firstnonspace = FALSE;
                    ++tfore;
                    while (isspace(*tfore))
                        ++tfore;
                    if (isalpha(*tfore))
                    {
                        tbuff_ptr = tok_buff;
                        *tbuff_ptr++ = '#';
                        while (isalpha(*tfore))
                            *tbuff_ptr++ = *tfore++;
                        *tbuff_ptr = '\0';
                        if (strcmp(tok_buff, "#include") == 0)
                            got_include = TRUE;
                        *lnum = line_count;
                        *defn = ((parentheses == 0) && (braces == 0));
                        return tok_buff;
                    }
                }
                firstnonspace = FALSE;
                ++tfore;
                continue;
            case '<':
                firstnonspace = FALSE;
                if (got_include && (braces == 0) && (parentheses == 0))
                {
                    ++tfore;
                    flush();
                    while (isspace(*tfore))
                        ++tfore;
                    tbuff_ptr = tok_buff;
                    while (*tfore != '>')
                        *tbuff_ptr++ = *tfore++;
                    *tbuff_ptr = '\0';
                    got_include = FALSE;
                    bump_tfore = TRUE;
                    *lnum = line_count;
                    *defn = ((parentheses == 0) && (braces == 0));
                    return tok_buff;
                }
                ++tfore;
                continue;
            case '"':
                firstnonspace = FALSE;
                if (got_include)
                {
                    ++tfore;
                    flush();
                    tbuff_ptr = tok_buff;
                    while (*tfore != '\"')
                        *tbuff_ptr++ = *tfore++;
                    *tbuff_ptr = '\0';
                    got_include = FALSE;
                    bump_tfore = TRUE;
                    *lnum = line_count;
                    *defn = ((parentheses == 0) && (braces == 0));
                    return tok_buff;
                }
                else
                {
                    for (;;)
                    {
                        ++tfore;
                        if (*tfore == '\"')
                            break;
                        if (escape_ch() == EOF)
                        {
                            return NULL;
                        }
                    }
                    ++tfore;
                }
                continue;
            default:
                firstnonspace = FALSE;
                ++tfore;
                continue;
        }
    }
}


/*******************************************************************************
       Name : scan_emit()
Description : Emit the token into the output file.
 Parameters : html - true if the token is to be surrounded with HTML
    Returns :
   Comments : If the token starts with '#' we remove the character from both
            : the filename and token reference.
*******************************************************************************/
void
scan_emit(bool html)
{
    if (html)
    {
        char *chptr;

        while ((chptr = strchr(tok_buff, '/')) != NULL)
        {
            *chptr = '-';
        }

        if (tok_buff[0] == '#')
        {
            fprintf(out, "<a href=\"%stoken__%s.html\">",
                         prefix, tok_buff+1);
        }
        else
        {
            fprintf(out, "<a href=\"%stoken_%s.html\">",
                         prefix, tok_buff);
        }
        flush();
        fprintf(out, "</a>");
    }
    else
    {
        flush();
    }
}


/*******************************************************************************
       Name :
Description :
 Parameters :
    Returns :
   Comments :
*******************************************************************************/
void
scan_close()
{
    fprintf(out, "</pre>\n");
    HTML_bodyfooter(out);

    fclose(in);
    fclose(out);
}

/*******************************************************************************
       Name :
Description :
 Parameters :
    Returns :
   Comments :
*******************************************************************************/
static void
flush(void)
{
    while (taft < tfore)
    {
        switch (*taft)
        {
            case '<':
                fprintf(out, "&lt;");
                break;
            default:
                fprintf(out, "%c", *taft);
                break;
        }
        ++taft;
    }
}
