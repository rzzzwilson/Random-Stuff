/******************************************************************************\
 *                                 L I S T . C                                *
 *                                =============                               *
 *                                                                            *
 *                                                                            *
\******************************************************************************/

#include "portable.h"

#include "list.h"
#include "scanner.h"
#include "utils.h"
#include "error.h"
#include "globals.h"

/******
 * Data structures.
 * The "LINE" structure is used to record each reference of a symbol
 ******/

typedef struct line
{
    struct line *next_line;
    int          line_number;
    bool         reference;
} LINE;


/******
 * The "ref_entry" structure establishes a symbol in the CREF tree
 * Each reference of the symbol (including the first) is noted in
 * a "line" structure hanging from the "lines" pointer.
 ******/

typedef struct ref_entry
{
    char             *name;
    char             *fname;
    LINE             *lines;
    struct ref_entry *left,
                     *right;
} REF_ENTRY;

/******
 * Local function prototypes.
 ******/

static void       add_line(REF_ENTRY *h_ptr, int lnum, bool refn);
static int        key_comp(REF_ENTRY *h_ptr, char *token, char *fname);
static REF_ENTRY *new_entry(char *token, char *fname, int lnum, bool defn);
static char      *new_str(char *str);
static void       print_node(REF_ENTRY *h_ptr);
static void       tokenlist_node(REF_ENTRY *h_ptr);

/******
 * Local variables
 ******/

static char      *codedir;              /* name of code directory        */
static int        max_symb;             /* max token length              */
static int        max_ref;              /* largest line number value     */
static REF_ENTRY *root;                 /* pointer to symbol tree        */
static int        line_cols;            /* # columns in line reference   */
static int        max_line;             /* # symbol refs per line        */
static int        page_width;           /* page width value              */
static int        max_file;             /* longest filename length       */
static char       old_symb[TOKBUFF_LEN];/* previous symbol buffer        */
static char       old_file[TOKBUFF_LEN];/* previous file name buffer     */
static FILE      *out_file;             /* FILE pointer for output file  */
static char       out_filename[FILENAME_LEN];
static char      *last_token;

/*******************************************************************************
       Name : list_open()
Description : Prepare the hcref list routines.
 Parameters : cdir - name of the code directory
            : pwidth - maximum page width in columns
    Returns :
   Comments :
*******************************************************************************/
void
list_open(char *cdir, int pwidth)
{
    codedir = cdir;
    max_symb = 0;
    max_ref = 0;
    max_file = 0;
    root = NULL;
    page_width = pwidth;
}


/*******************************************************************************
       Name : list_add()
Description : Add a symbol to the cref tree.
 Parameters : token - address of buffer holding token anme
            : fname - name of the file
            : lnum  - line number of token
            : defn  - true if this is a definition, else false
    Returns :
   Comments : It inserts a "LINE" reference if the symbol already exists in
            : the tree but generates a "REF_ENTRY" entry if this is the first
            : reference to the symbol and then adds a "LINE" entry.
*******************************************************************************/
void
list_add(char *token, char *fname, int lnum, bool defn)
{
    REF_ENTRY    *fore;
    REF_ENTRY    *aft;
    int           status;
    int           size;

/******
 * Check max sizes of strings for use later while printing
 ******/

    if ((size = strlen(fname)) > max_file)
        max_file = size;

    if ((size = strlen(token)) > max_symb)
        max_symb = size;

    if (lnum > max_ref)
        max_ref = lnum;

/******
 * Insert into tree
 ******/

    if (root == NULL)             /* if tree empty, easy */
    {
        root = new_entry(token, fname, lnum, defn);
        return;
    }

/******
 *  If tree not empty, walk through the tree looking for right place
 ******/

    fore = root;
    for (;;)
    {
        if ((status = key_comp(fore, token, fname)) > 0)
        {
            aft = fore;
            if ((fore = fore->left) == NULL)
            {
                aft->left = new_entry(token, fname, lnum, defn);
                return;
            }
        }
        else if (status < 0)
        {
            aft = fore;
            if ((fore = fore->right) == NULL)
            {
                aft->right = new_entry(token, fname, lnum, defn);
                return;
            }
        }
        else                              /* found!, add "LINE" */
        {
            add_line(fore, lnum, defn);
            return;
        }
    }
}


/*******************************************************************************
       Name : list_cref()
Description : Output the individual cress-reference listing for each token.
 Parameters :
    Returns :
   Comments : The files are created in the code directory ("cdir") and will
            : be broken up into many files each containing individual tokens
            : and its cross-reference.
*******************************************************************************/
void list_cref(void)
{
    if (root == NULL)
        return;

    line_cols = 0;

    while (max_ref)
    {
        ++line_cols;
        max_ref /= 10;
    }

    max_line = page_width - (max_symb+2) - (max_file+2);
    if (max_line < MIN_LINE)
        error("Sorry, page width is too small to proceed.  "
              "Try '-w%d' at least\n", 
              page_width - max_line + MIN_LINE);

    max_line /= line_cols + 2;
    max_file = max(8, max_file);

    strcpy(out_filename, "");
    print_node(root);

    if (strlen(out_filename) > 0)
        HTML_bodyfooter(out_file);
}


/*******************************************************************************
       Name : list_tokenlist()
Description : Dump the listing of tokens to the output files.
 Parameters :
    Returns :
   Comments : The files are created in the code directory ("cdir") and will
            : be broken up into many files each containing all tokens that
            : start with the same letter, with links to each token
            : cross-reference listing.
*******************************************************************************/
void list_tokenlist(void)
{
    if (root == NULL)
        return;

    strcpy(old_symb, "");

    strcpy(out_filename, "");
    tokenlist_node(root);

    if (strlen(out_filename) > 0)
        HTML_bodyfooter(out_file);
}


/*******************************************************************************
       Name :
Description :
 Parameters :
    Returns :
   Comments :
*******************************************************************************/
void
list_menu(FILE *out, char *outputdir, REF_ENTRY *rptr)
{
    if (rptr == NULL)                  /* empty sub-tree - return */
        return;

    list_menu(out, outputdir, rptr->left);

    if (tolower(*rptr->name) != tolower(*last_token))
    {
        if (*rptr->name == '#')
            fprintf(out, "<TD><A HREF=\"tlist_.html\" "
                         "TARGET=\"view\">#</A></BIG></TD>\n");
        else
            fprintf(out, "<TD><A HREF=\"tlist_%c.html\" "
                         "TARGET=\"view\">%c</A></BIG></TD>\n",
                         toupper(*rptr->name), toupper(*rptr->name));

        last_token = rptr->name;
    }

    list_menu(out, outputdir, rptr->right);
}


/*******************************************************************************
       Name :
Description :
 Parameters :
    Returns :
   Comments :
*******************************************************************************/
void
list_menuhtml(FILE *out, char *outputdir)
{
    if (root == NULL)
        return;

    last_token = "";
    list_menu(out, outputdir, root);
}


/*******************************************************************************
       Name :
Description :
 Parameters :
    Returns :
   Comments :
*******************************************************************************/
void
list_close(void)
{

}

/*******************************************************************************
       Name : add_line()
Description : Add line reference to pre-existing token reference.
 Parameters : h_ptr - address of REF_ENTRY to add line to
            : lnum  - the line number to add
    Returns :
   Comments :
*******************************************************************************/
static void
add_line(REF_ENTRY *h_ptr, int lnum, bool defn)
{
    LINE *l_ptr;

    if (h_ptr->lines && (h_ptr->lines->line_number == lnum))
        return;

    l_ptr = new(LINE);
    l_ptr->line_number = lnum;
    l_ptr->next_line = h_ptr->lines;
    l_ptr->reference = defn;
    h_ptr->lines = l_ptr;
}


/*******************************************************************************
       Name : new_entry()
Description : Creates a new symbol reference entry.
 Parameters : token - address of buffer holding token
            : fname - string holding filename
            : lnum  - line number in above file
            : defn  - true if a definition, else false
    Returns : Address of the new entry.
   Comments :
*******************************************************************************/
static REF_ENTRY *
new_entry(char *token, char *fname, int lnum, bool defn)
{
    REF_ENTRY *h_ptr;

    h_ptr = new(REF_ENTRY);
    h_ptr->name = new_str(token);
    h_ptr->fname = new_str(fname);
    h_ptr->lines = NULL;
    h_ptr->left = NULL;
    h_ptr->right = NULL;

    add_line(h_ptr, lnum, defn);

    return h_ptr;
}


/*******************************************************************************
       Name : new_str()
Description : Clone a string in newly allocated memory.
 Parameters : str - the string to clone
    Returns : Address of teh clone string.
   Comments :
*******************************************************************************/
static char *
new_str(char *str)
{
    char *s_ptr;

    s_ptr = (char *) calloc(1, strlen(str)+1);
    strcpy(s_ptr, str);

    return s_ptr;
}


/*******************************************************************************
       Name : key_comp()
Description : Compares the token passed with that in a REF_ENTRY.
 Parameters : h_ptr - REF_ENTRY address
            : token - address of buffer containing token string
    Returns :
   Comments : Returns <0, 0 or >0 if "token" is < = > REF_ENTRY.
*******************************************************************************/
static int
key_comp(REF_ENTRY *h_ptr, char *token, char *fname)
{
    int  status;

    status = Ustrcmp(h_ptr->name, token);
    if (status != 0)
        return status;

    status = strcmp(h_ptr->name, token);
    if (status != 0)
        return status;

    return strcmp(h_ptr->fname, fname);
}


/*******************************************************************************
       Name : print_info()
Description : Print the info held in the passed REF_ENTRY.
 Parameters : h_ptr - address of the REF_ENTRY to print
    Returns :
   Comments : 'old_symb' and 'old_file' are updated for each line to help
            : format the lines.
*******************************************************************************/
static void
print_info(REF_ENTRY *h_ptr)
{
    int   i;
    LINE *aft;
    LINE *mid;
    LINE *fore;
    char  new_filename[FILENAME_LEN];
    char  tokint[FILENAME_LEN];
    char  buff[FILENAME_LEN];
    char *chptr;

/******
 * Reverse chain of line references so they print out in correct order.
 ******/

    aft = NULL;
    mid = h_ptr->lines;
    fore = mid->next_line;
    while (fore != NULL)
    {
        mid->next_line = aft;
        aft = mid;
        mid = fore;
        fore = mid->next_line;
    }
    mid->next_line = aft;
    h_ptr->lines = mid;

/******
 * Change the token name to get around tokens containing '/'.
 ******/

    strcpy(tokint, h_ptr->name);
    while ((chptr = strchr(tokint, '/')) != NULL)
    {
        *chptr = '-';
    }

/******
 * Here we must decide if the token to print requires a new output filename.
 * 'new_filename' holds the output filename currently open.
 * (zero length string if nothing currently open).
 ******/

    if (*tokint == '#')
    {
        *tokint = '_';
        sprintf(new_filename, "%s/token_%s.html", codedir, tokint);
        *tokint = '#';
    }
    else
        sprintf(new_filename, "%s/token_%s.html", codedir, tokint);

    if (strcmp(new_filename, out_filename) != 0)
    {
        if (strlen(out_filename) != 0)
        {
            fprintf(out_file, "</pre>\n");
            HTML_bodyfooter(out_file);
            fclose(out_file);
        }

        strcpy(out_filename, new_filename);
        out_file = fopen(out_filename, "w");
        if (out_file == NULL)
        {
            error("Can't open '%s' for output: %s\n", strerror(errno));
            exit(1);
        }

        sprintf(buff, "token: %s", h_ptr->name);
        HTML_bodyheader(out_file, buff);
        fprintf(out_file, "<pre>\n");
    }

/******
 * Now print the line references out.
 ******/

    for (;;)
    {
        char link[100];
        int  count;

        if (h_ptr->lines == NULL)
            return;

        sprintf(link, "<a href=\"%s.html#line1\" target=\"view\">",
                      h_ptr->fname);

        if (strcmp(h_ptr->name, old_symb) != 0)
        {
            count = max_symb - strlen(h_ptr->name) + 2;
            fprintf(out_file, "<a name=\"%s\">", tokint);
            fprintf(out_file, "%s", h_ptr->name);
            fprintf(out_file, "</a>");

            while (count--)
                fprintf(out_file, " ");

            count = max_file - strlen(h_ptr->fname) + 2;
            fprintf(out_file, link);
            fprintf(out_file, "%s", h_ptr->fname);
            fprintf(out_file, "</a>");

            while (count--)
                fprintf(out_file, " ");
        }
        else if (strcmp(h_ptr->fname, old_file) != 0)
        {
            count = max_symb + 2;
            while (count--)
                fprintf(out_file, " ");

            count = max_file - strlen(h_ptr->fname) + 2;
            fprintf(out_file, link);
            fprintf(out_file, "%s", h_ptr->fname);
            fprintf(out_file, "</a>");

            while (count--)
                fprintf(out_file, " ");
        }
        else
        {
            count = max_symb + 2;
            while (count--)
                fprintf(out_file, " ");

            count = max_file + 2;
            while (count--)
                fprintf(out_file, " ");
        }

        strcpy(old_symb, h_ptr->name);
        strcpy(old_file, h_ptr->fname);

    /******
     * Now print the line references.
     ******/

        for (i = max_line; i; --i)
        {
            char link[100];
            int  count;

            if (h_ptr->lines == NULL)
            {   if (i != max_line)
                    fprintf(out_file, "\n");
                return;
            }

            sprintf(link, "%d", h_ptr->lines->line_number);

            count = line_cols - strlen(link) + 1;
            fprintf(out_file, "<a href=\"%s.html#line%d\" target=\"view\">",
                              h_ptr->fname, h_ptr->lines->line_number);
            fprintf(out_file, "%s%d%s", h_ptr->lines->reference ? "<b>" : "",
                                        h_ptr->lines->line_number, 
                                        h_ptr->lines->reference ? "</b>" : ""
                   );
            fprintf(out_file, "</a>");

            while (count--)
                fprintf(out_file, " ");

            h_ptr->lines = h_ptr->lines->next_line;
        }

        fprintf(out_file, "\n");
    }
}


/*******************************************************************************
       Name : tokenlist_info()
Description : Print the info held in the passed REF_ENTRY.
 Parameters : h_ptr - address of the REF_ENTRY to print
    Returns :
   Comments : 'old_symb' and 'old_file' are updated for each line to help
            : format the lines.
*******************************************************************************/
static void
tokenlist_info(REF_ENTRY *h_ptr)
{
    char *chptr;
    char  new_filename[FILENAME_LEN];
    char  tokint[FILENAME_LEN];
    char  buff[FILENAME_LEN];

/******
 * Change the token name to get around tokens containing '/'.
 ******/

    strcpy(tokint, h_ptr->name);
    while ((chptr = strchr(tokint, '/')) != NULL)
    {
        *chptr = '-';
    }

/******
 * Here we must decide if the token to print requires a new output filename.
 * 'new_filename' holds the output filename currently open.
 * (zero length string if nothing currently open).
 ******/

    if (*tokint == '#')
        sprintf(new_filename, "%s/tlist_.html", codedir);
    else
        sprintf(new_filename, "%s/tlist_%c.html", codedir, toupper(*tokint));

    if (strcmp(new_filename, out_filename) != 0)
    {
        if (strlen(out_filename) != 0)
        {
            fprintf(out_file, "</pre>\n");
            HTML_bodyfooter(out_file);
            fclose(out_file);
        }

        strcpy(out_filename, new_filename);
        out_file = fopen(out_filename, "w");
        if (out_file == NULL)
        {
            error("Can't open '%s' for output: %s\n", strerror(errno));
            exit(1);
        }

        sprintf(buff, "tokens: %c...", *h_ptr->name);
        HTML_bodyheader(out_file, buff);
        fprintf(out_file, "<pre>\n");
    }

/******
 * Now 'new_filename' will contain the name for the token cref file.
 ******/

    if (*tokint == '#')
    {
        *tokint = '_';
        sprintf(new_filename, "token_%s.html", tokint);
        *tokint = '#';
    }
    else
        sprintf(new_filename, "token_%s.html", tokint);

/******
 * Now print the token out.
 ******/

    if (strcmp(old_symb, h_ptr->name) != 0)
    {
        fprintf(out_file,
                "\t<a href=\"%s#line1\" target=\"view\">"
                "%s"
                "</a>\n",
                new_filename,
                h_ptr->name);
        strcpy(old_symb, h_ptr->name);
    }
}


/*******************************************************************************
       Name : print_node()
Description : Do a pre-order walk through the list tree and call print_info()
            : for each leaf node.
 Parameters : h_ptr - the tree (or sub-tree) address
    Returns :
   Comments :
*******************************************************************************/
static void
print_node(REF_ENTRY *h_ptr)
{
    if (h_ptr == NULL)                  /* empty sub-tree - return */
        return;

    print_node(h_ptr->left);

    print_info(h_ptr);

    print_node(h_ptr->right);
}


/*******************************************************************************
       Name : print_node()
Description : Do a pre-order walk through the list tree and call print_info()
            : for each leaf node.
 Parameters : h_ptr - the tree (or sub-tree) address
    Returns :
   Comments :
*******************************************************************************/
static void
tokenlist_node(REF_ENTRY *h_ptr)
{
    if (h_ptr == NULL)                  /* empty sub-tree - return */
        return;

    tokenlist_node(h_ptr->left);

    tokenlist_info(h_ptr);

    tokenlist_node(h_ptr->right);
}
