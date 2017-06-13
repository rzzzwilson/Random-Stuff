/******************************************************************************\
 *                            M E M C H E C K . C                             *
 *                           =====================                            *
 *                                                                            *
 *   This suite of functions is used to track down those nasty memory         *
 *   allocation errors like:                                                  *
 *                                                                            *
 *        . not freeing memory before program exit                            *
 *        . freeing memory twice                                              *
 *        . memory overruns (accessing past the end of the allocated block)   *
 *        . memory underruns (accessing before the start of the block)        *
 *        . changing the contents of a block after freeing it                 *
 *                                                                            *
 *   How do you use these functions? Just #include memcheck.h into your       *
 *   program and place the function MCinit() at the start of your main()      *
 *   and MCterm() at the end of main() code. You may place MCcheck()          *
 *   anywhere in your program for a check of memory similar to the one        *
 *   you get from MCterm().                                                   *
 *                                                                            *
 *   Your program will now compile and behave as before. The routines in      *
 *   this file are not being used. To turn on the checking, #define the       *
 *   label MCDEBUG.                                                           *
 *                                                                            *
 *   You may pass flags like MC_VERBOSE to MCinit() to control the blow-      *
 *   by-blow commentary.                                                      *
 *                                                                            *
 *   For example, a simple program might look like:                           *
 *                                                                            *
 *       #define MCDEBUG     // remove this to turn off checking              *
 *       #include <memcheck.h>                                                *
 *                                                                            *
 *       void main(void)                                                      *
 *       {                                                                    *
 *           MCinit(0, NULL);                                                 *
 *              .                                                             *
 *              .                                                             *
 *              .                                                             *
 *       }                                                                    *
 *                                                                            *
 *    Note that MCinit() sets up (through atexit()) an execution of the       *
 *    MCterm() function at the end of main(). The user is free to call        *
 *    MCterm() before program termination.                                    *
 *                                                                            *
\******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define MCDEBUG
#include "memcheck.h"


/******
 * Turn off macros for this module!
 ******/

#undef malloc
#undef calloc
#undef free
#undef realloc


/******
 * Define internal types.
 ******/

typedef short       BOOL;


/******
 * Define the main memory checking structure.
 ******/

typedef struct memchain
{
    struct memchain *m_next;                    /* next MEMCHAIN block    */
    void            *m_addr;                    /* user alloced addr      */
    void            *m_block;                   /* actual allocated mem   */
    size_t           m_size;                    /* requested size         */
    char            *m_afile;                   /* alloc file name        */
    size_t           m_aline;                   /* alloc file line        */
    char            *m_ffile;                   /* free file name         */
    size_t           m_fline;                   /* free file line         */
} MEMCHAIN;


/******
 * Define various values:
 *    Size of hashtable.
 *    Value used to trash supposedly "unused" memory.
 *    Boolean values.
 ******/

#define HASH_SIZE     999911            /* prime number? */

#define TRASHVALUE    0xff

#define TRUE          1
#define FALSE         0


/******
 * Global variables.
 ******/

static MEMCHAIN *MCallocated[HASH_SIZE];    /* allocated hash table  */
static MEMCHAIN *MCfreed[HASH_SIZE];        /* freed hash table      */

static BOOL     MCverbose;                      /* verbose if TRUE       */

static char     MCcheckblock[CHECKSIZE];        /* underrun/overrun test */
                                                /* block comparison      */

static void mycallback(char *fmt, ...);
static CALLBACK *callback = mycallback;

static BOOL     setup = FALSE;


/******************************************************************************
 FUNCTION    : mycallback()
 DESCRIPTION : Provides a default callback routine.
 PARAMETERS  : fmt - printf-style format string
             : ...
 RETURNS     : void
 COMMENTS    : 
 ******************************************************************************/
static void
mycallback(char *fmt, ...)
{
   va_list args;

   va_start(args, fmt);
   vfprintf(stdout, fmt, args);
   va_end(args);

   fflush(stdout);
}


/******************************************************************************
 FUNCTION    : nullcallback()
 DESCRIPTION : Provides a null callback routine.
 PARAMETERS  : fmt - printf-style format string
             : ...
 RETURNS     : void
 COMMENTS    : Does nothing.
 ******************************************************************************/
static void
nullcallback(char *fmt, ...)
{
}


/******************************************************************************
 FUNCTION    : addMCchain()
 DESCRIPTION : Add a MEMCHAIN item to a hash table.
 PARAMETERS  : chain - base address of hash table
             : new   - pointer to MEMCHAIN to add to 'chain'
 RETURNS     : void
 COMMENTS    : 'new->m_next' is assumed NULL.
             : Because most allocation routines return pointers on a 4 or 8
             : byte alignment, we ignore the low 4 bits of the address when
             : hashing.
 ******************************************************************************/
static void
addMCchain(MEMCHAIN *chain[], MEMCHAIN *new)
{
    long     index = (long) new->m_addr % HASH_SIZE;
    MEMCHAIN *aft;
    MEMCHAIN *fore;

/******
 * If no MEMCHAIN items in the list, add new as first, return.
 ******/

    if (chain[index] == NULL)
    {
        chain[index] = new;
        return;
    }

/******
 * Bucket list not empty, find correct insertion point.
 ******/

    aft = chain[index];
    fore = aft->m_next;

    if (fore == NULL)
    {		/* only one in list, insert before or after? */
        if (aft->m_addr < new->m_addr)
        {
            new->m_next = aft;
            chain[index] = new;
        }
        else
        {
            aft->m_next = new;
        }
    }
    else
    {
        while (fore != NULL && (fore->m_addr > new->m_addr))
        {
            aft = fore;
            fore = fore->m_next;
        }
        new->m_next = fore;
        aft->m_next = new;
    }
}


/******************************************************************************
 FUNCTION    : lookupMCchain()
 DESCRIPTION : Finds a MEMCHAIN matching the block address given.
 PARAMETERS  : chain - chain to look in
             : addr  - user address to look for
 RETURNS     : NULL if not found, else address of found MEMCHAIN.
 COMMENTS    : Because most allocation routines return pointers on a 4 or 8
             : byte alignment, we ignore the low 4 bits of the address when
             : hashing.
 ******************************************************************************/
static MEMCHAIN *
lookupMCchain(MEMCHAIN *chain[], void *addr)
{
    long     index = (long) addr % HASH_SIZE;
    MEMCHAIN *scan;
    MEMCHAIN *result = NULL;

    for (scan = chain[index]; scan != NULL && scan->m_addr <= addr; scan = scan->m_next)
    {
        if (scan->m_addr == addr)
        {
            result = scan;
            break;
        }
    }
     
    return result;
}


/******************************************************************************
 FUNCTION    : removeMCchain()
 DESCRIPTION : Remove a MEMCHAIN block from the given chain.
 PARAMETERS  : chain - the chain to remove from
             : block - address of MEMCHAIN block to remove from chain
 RETURNS     : void
 COMMENTS    : We assume that the 'block' block does exist in the chain.
             : The m_next pointer is nulled on removal, in case we add to
             : another chain.
             : Because most allocation routines return pointers on a 4 or 8
             : byte alignment, we ignore the low 4 bits of the address when
             : hashing.
 ******************************************************************************/
static void
removeMCchain(MEMCHAIN *chain[], MEMCHAIN *block)
{
    long     index = (long) block->m_addr % HASH_SIZE;
    MEMCHAIN *aft;
    MEMCHAIN *fore;

    aft = chain[index];
    fore = aft->m_next;

    if (aft == block)
    {
        chain[index] = aft->m_next;
        block->m_next = NULL;
        return;
    }

    while (fore != block)
    {
        aft = fore;
        fore = fore->m_next;
    }

    aft->m_next = fore->m_next;
    block->m_next = NULL;
}


/******************************************************************************
 FUNCTION    : MCinit()
 DESCRIPTION : Initializes the MEMCHECK system.
 PARAMETERS  : flags - bitmap of various memcheck control flags
             : cback - address of callback routine called on error
 RETURNS     : void
 COMMENTS    : Just sets up the allocated and free chains to empty.
 ******************************************************************************/
void
MCinit(unsigned flags, CALLBACK *cback)
{
    int i;

    if (setup != FALSE)
    {
        fprintf(stderr, "MCinit() called twice\n");
        exit(EXIT_FAILURE);
    }

    setup = TRUE;

    if (cback == NULL)
        callback = nullcallback;
    else
        callback = cback;

    for (i = 0; i < HASH_SIZE; ++i)
    {
        MCallocated[i] = NULL;
        MCfreed[i] = NULL;
    }

    memset(MCcheckblock, TRASHVALUE, CHECKSIZE);

    MCverbose = flags & MC_VERBOSE;

    atexit(MCterm);
}


/******************************************************************************
 FUNCTION    : MCmemalloc()
 DESCRIPTION : Gets desired memory and notes the details.
 PARAMETERS  : file - name of the file containing the call
             : line - line of the file .....
             : size - size of desired block in bytes
             : name - address of name of caller string
 RETURNS     : The address of the allocated block.
 COMMENTS    : Service routine.
 ******************************************************************************/
static void *
MCmemalloc(char *file, unsigned line, unsigned size, char *name)
{
    MEMCHAIN *new = malloc(sizeof(MEMCHAIN));

    if (!new)
    {
        if (MCverbose)
            callback("%7s: Unsuccessful at %4d in %s\n", name, line, file);

        return NULL;
    }

    new->m_afile = file;                        /* create new structure     */
    new->m_aline = line;                        /* for this allocated block */
    new->m_ffile = "";
    new->m_fline = 0;
    new->m_size  = size;
    new->m_next = NULL;
    new->m_block = malloc(size + 2 * CHECKSIZE);
    if (!new->m_block)
    {
        if (MCverbose)
            callback("%7s: Unsuccessful at %4d in %s\n", name, line, file);

        free(new);

        return NULL;
    }
    memset(new->m_block, TRASHVALUE, size + 2 * CHECKSIZE);

    new->m_addr  = (char *) new->m_block + CHECKSIZE;

/******
 * Add new MEMCHAIN structure to 'allocated' hash table.
 ******/

    addMCchain(MCallocated, new);

    if (MCverbose)
        callback("%7s: %3d bytes (%8.8p) at %4d in %s\n",
                 name, size, new->m_addr, line, file);

    return new->m_addr;
}


/******************************************************************************
 FUNCTION    : MCmalloc()
 DESCRIPTION : Replaces C library malloc().
             : Gets desired memory and notes the details.
 PARAMETERS  : file - name of the file containing the call
             : line - line of the file .....
             : size - size of desired block in bytes
 RETURNS     : The address of the allocated block.
 COMMENTS    : "file" and "line" supplied by malloc() macro.
 ******************************************************************************/
void *
MCmalloc(char *file, unsigned line, unsigned size)
{
    if (setup == FALSE)
    {
        fprintf(stderr, "MCinit() must be called first\n");
        exit(EXIT_FAILURE);
    }

    return MCmemalloc(file, line, size, "malloc");
}


/******************************************************************************
 FUNCTION    : MCcalloc()
 DESCRIPTION : Replaces C library calloc().
             : Gets desired memory, clears it and notes the details.
 PARAMETERS  : file - name of the file containing the call
             : line - line of the file .....
             : num  - number of elements
             : size - size of desired element in bytes
 RETURNS     : The address of the allocated block.
 COMMENTS    : "file" and "line" supplied by calloc() macro.
 ******************************************************************************/
void *
MCcalloc(char *file, unsigned line, unsigned num, unsigned size)
{
    void *block;

    if (setup == FALSE)
    {
        fprintf(stderr, "MCinit() must be called first\n");
        exit(EXIT_FAILURE);
    }

    block = MCmemalloc(file, line, num * size, "calloc");

    memset(block, 0, size);

    return block;
}


/******************************************************************************
 FUNCTION    : MCsizeof()
 DESCRIPTION : Get user size of block given user address.
 PARAMETERS  : block - address of block to get size for
 RETURNS     : The user size in bytes. 0 if block not found.
 COMMENTS    : Service routine.
 ******************************************************************************/
static unsigned
MCsizeof(void *block)
{
    MEMCHAIN *found;

/******
 * Do lookup to find allocated block.
 ******/

    found = lookupMCchain(MCallocated, block);
    if (found != NULL)
        return found->m_size;

    return 0;            /* not found, return 0 size */
}


/******************************************************************************
 FUNCTION    : MCmemfree()
 DESCRIPTION : Free a memory block and note the details.
 PARAMETERS  : file  - name of the file containing the call
             : line  - line of the file .....
             : block - address of block to free
             : name  - address of operation name string
 RETURNS     : void.
 COMMENTS    : Service routine.
 ******************************************************************************/
static void
MCmemfree(char *file, unsigned line, void *block, char *name)
{
    MEMCHAIN *found;

    if (setup == FALSE)
    {
        fprintf(stderr, "MCinit() must be called first\n");
        exit(EXIT_FAILURE);
    }

/******
 * Look for the block being freed in "allocated" chain.  If found, move
 * to 'freed' chain.  If not found, report error.
 ******/

    found = lookupMCchain(MCallocated, block);
    if (found != NULL)
    {
        found->m_ffile = file;
        found->m_fline = line;

        /******
         * Move from 'allocated' to 'freed' chain.
         ******/

        removeMCchain(MCallocated, found);
        addMCchain(MCfreed, found);

        if (MCverbose)
            callback("%7s: %3d bytes (%8.8p) at %4d of %s\n",
                     name, found->m_size, block, found->m_aline, found->m_afile);

        if (memcmp(MCcheckblock, found->m_block, CHECKSIZE))
            callback("%7s: underrun %3d bytes (%8.8p) allocd at %4d in %s,\n"
                     "                                          freed at %4d in %s\n",
                     name, found->m_size, found->m_addr,
                     found->m_aline, found->m_afile,
                     found->m_fline, found->m_ffile);

        if (memcmp(MCcheckblock,
                   (char *) found->m_block + CHECKSIZE + found->m_size,
                   CHECKSIZE
                  )
           )
            callback("%7s: overrun  %3d bytes (%8.8p) allocd at %4d in %s,\n"
                     "                                          freed at %4d in %s\n",
                     name, found->m_size, found->m_addr,
                     found->m_aline, found->m_afile,
                     found->m_fline, found->m_ffile);

        memset(found->m_block, TRASHVALUE, found->m_size + 2 * CHECKSIZE);

        return;
    }

/******
 * If block *not* found in "allocated" chain, look for block in "freed"
 * chain - double free()!
 ******/

    found = lookupMCchain(MCfreed, block);
    if (found != NULL)
    {
        callback("%7s: twice    %3d bytes (%8.8p) allocd at %4d in %s,\n"
                 "                                          freed at %4d in %s,\n"
                 "                                     then freed at %4d in %s\n",
                 name, found->m_size, found->m_addr,
                 found->m_aline, found->m_afile,
                 found->m_fline, found->m_ffile,
                 line, file);

        return;
    }

/******
 * If none of above - never allocated error!
 ******/

    callback("%7s: unallocated block  (%8.8p)  freed at %4d in %s\n", name, block, line, file);
}


/******************************************************************************
 FUNCTION    : MCfree()
 DESCRIPTION : Free a memory block and note the details.
             : Replaces library free().
 PARAMETERS  : file - name of the file containing the call
             : line - line of the file .....
             : size - size of desired element in bytes
 RETURNS     : void.
 COMMENTS    : "file" and "line" supplied by free() macro.
 ******************************************************************************/
void
MCfree(char *file, unsigned line, void *block)
{
    if (setup == FALSE)
    {
        fprintf(stderr, "MCinit() must be called first\n");
        exit(EXIT_FAILURE);
    }

    MCmemfree(file, line, block, "free");
}


/******************************************************************************
 FUNCTION    : MCrealloc()
 DESCRIPTION : Free a memory block and alloc new block.
             : Replaces library realloc().
 PARAMETERS  : file  - name of the file containing the call
             : line  - line of the file .....
             : block - address of block to free
             : size  - size of desired new block in bytes
 RETURNS     : Address of new block.
 COMMENTS    : "file" and "line" supplied by realloc() macro.
 ******************************************************************************/
void *
MCrealloc(char *file, unsigned line, void *block, unsigned size)
{
    void     *new;
    unsigned oldsize;
    unsigned newsize;

    if (setup == FALSE)
    {
        fprintf(stderr, "MCinit() must be called first\n");
        exit(EXIT_FAILURE);
    }

    oldsize = MCsizeof(block);
    if (!oldsize)
    {
        callback("realloc: unallocated block (%8.8p) at %4d in %s\n", block, line, file);

        return NULL;
    }

    new = MCmemalloc(file, line, size, "realloc");
    if (!new)
    {
        if (MCverbose)
            callback("realloc: unsuccessful at %4d in %s\n", line, file);

        return NULL;
    }

    newsize = size;
    if (size < oldsize)
        newsize = oldsize;
    memcpy(new, block, newsize);

    MCmemfree(file, line, block, "free");

    if (MCverbose)
        callback("realloc: %3d bytes (%8.8p) converted to\n"
                 "         %3d bytes (%8.8p) at line %4d in %s\n",
                 oldsize, block, size, new, line, file);

    return new;
}


/******************************************************************************
 FUNCTION    : MCcheck()
 DESCRIPTION : Look at free and allocated chains and report any problems.
 PARAMETERS  : void.
 RETURNS     : void.
 COMMENTS    : Call this function to pin down any errors you suspect.
 ******************************************************************************/
void
MCcheck(void)
{
    int      i;
    MEMCHAIN *scan;

    if (setup == FALSE)
    {
        fprintf(stderr, "MCinit() must be called first\n");
        exit(EXIT_FAILURE);
    }

/******
 * Report on memory allocated and not yet freed.
 ******/

    callback("+--- check blocks not yet free ----\n");

    for (i = 0; i < HASH_SIZE; ++i)
    {
        for (scan = MCallocated[i]; scan != NULL; scan = scan->m_next)
        {
            callback("allocated: %3d bytes (%8.8p)        at %4d in %s\n",
                     scan->m_size, scan->m_addr, scan->m_aline, scan->m_afile);

            if (memcmp(MCcheckblock, scan->m_block, CHECKSIZE))
                callback(" underrun: %3d bytes (%8.8p) allocated at %4d in %s\n",
                         scan->m_size, scan->m_addr, scan->m_aline, scan->m_afile);

            if (memcmp(MCcheckblock,
                       (char *) scan->m_block + CHECKSIZE + scan->m_size,
                       CHECKSIZE
                      )
               )
                callback("  overrun: %3d bytes (%8.8p) allocated at %4d in %s\n",
                         scan->m_size, scan->m_addr, scan->m_aline, scan->m_afile);
        }
    }

/******
 * Report on memory freed but changed *after* free()!
 ******/

    callback("+--- blocks changed after free ----\n");

    for (i = 0; i < HASH_SIZE; ++i)
    {
        for (scan = MCfreed[i]; scan != NULL; scan = scan->m_next)
        {
            unsigned char *ptr = scan->m_addr;
            int           count = scan->m_size;

            while (count--)
            {
                if (*ptr != TRASHVALUE)
                {
                    callback("  changed: %3d bytes (%8.8p) allocated %d in %s,\n"
                             "                                   freed %d in %s\n",
                             scan->m_size, scan->m_addr,
                             scan->m_aline, scan->m_afile,
                             scan->m_fline, scan->m_ffile);
    
                    break;
                }

                ++ptr;
            }

            if (memcmp(MCcheckblock, scan->m_block, CHECKSIZE))
                callback(" underrun: %3d bytes (%8.8p) allocated at %4d in %s,\n"
                         "                                   freed at %4d in %s\n",
                         scan->m_size, scan->m_addr,
                         scan->m_aline, scan->m_afile,
                         scan->m_fline, scan->m_ffile);

            if (memcmp(MCcheckblock,
                       (char *) scan->m_block + CHECKSIZE + scan->m_size,
                       CHECKSIZE
                      )
               )
                callback("  overrun: %3d bytes (%8.8p) allocated at %4d in %s,\n"
                         "                                   freed at %4d in %s\n",
                         scan->m_size, scan->m_addr,
                         scan->m_aline, scan->m_afile,
                         scan->m_fline, scan->m_ffile);
        }
    }
    
    callback("+--------- end of check -----------\n");
}


/******************************************************************************
 FUNCTION    : MCterm()
 DESCRIPTION : Close down the MEMCHECK system & report problems.
 PARAMETERS  : void.
 RETURNS     : void.
 COMMENTS    : Usually called 'atexit'.
 ******************************************************************************/
void
MCterm(void)
{
    MEMCHAIN *scan;
    long     i;

/******
 * Check the 'setup' flag - if FALSE, assume MCterm() called twice.
 ******/

    if (setup == FALSE)
        return;

    setup = FALSE;

/******
 * Report on memory never freed.
 ******/

    callback("+---- check blocks not yet free ----\n");

    for (i = 0; i < HASH_SIZE; ++i)
    {
        for (scan = MCallocated[i]; scan != NULL; scan = scan->m_next)
        {
            callback("allocated: %3d bytes (%8.8p)        at %4d in %s\n",
                     scan->m_size, scan->m_addr,
                     scan->m_aline, scan->m_afile);

            if (memcmp(MCcheckblock, scan->m_block, CHECKSIZE))
                callback(" underrun: %3d bytes (%8.8p) allocd at %4d in %s\n",
                         scan->m_size, scan->m_addr,
                         scan->m_aline, scan->m_afile);

            if (memcmp(MCcheckblock,
                       (char *) scan->m_block + CHECKSIZE + scan->m_size,
                       CHECKSIZE
                      )
               )
                callback("  overrun: %3d bytes (%8.8p) allocd at %4d in %s\n",
                         scan->m_size, scan->m_addr,
                         scan->m_aline, scan->m_afile);
        }
    }

/******
 * Checked for changed blocks in "freed" chain.
 ******/

    callback("+---- blocks changed after free ----\n");

    for (i = 0; i < HASH_SIZE; ++i)
    {
        for (scan = MCfreed[i]; scan != NULL; scan = scan->m_next)
        {
            unsigned char *ptr = scan->m_addr;
            int           count = scan->m_size;

            while (count--)
            {
                if (*ptr != TRASHVALUE)
                {
                    callback("  changed: %3d bytes (%8.8p) allocd at %4d in %s,\n"
                             "                                   freed at %4d in %s\n",
                             scan->m_size, scan->m_addr,
                             scan->m_aline, scan->m_afile,
                             scan->m_fline, scan->m_ffile);
                    break;
                }

                ++ptr;
            }

            if (memcmp(MCcheckblock, scan->m_block, CHECKSIZE))
                callback(" underrun: %3d bytes (%8.8p) allocated at %4d in %s,\n"
                         "                                   freed at %4d in %s\n",
                         scan->m_size, scan->m_addr,
                         scan->m_aline, scan->m_afile,
                         scan->m_fline, scan->m_ffile);

            if (memcmp(MCcheckblock,
                       (char *) scan->m_block + CHECKSIZE + scan->m_size,
                       CHECKSIZE
                      )
               )
                callback("  overrun: %3d bytes (%8.8p) allocd at %4d in %s,\n"
                         "                                 freed at %4d in %s\n",
                         scan->m_size, scan->m_addr,
                         scan->m_aline, scan->m_afile,
                         scan->m_fline, scan->m_ffile);
        }
    }

/******
 * Free all memory in "allocated" chain.
 ******/

    for (i = 0; i < HASH_SIZE; ++i)
    {
        for (scan = MCallocated[i]; scan != NULL; )
        {
            MEMCHAIN *next = scan->m_next;

            free(scan->m_block);
            free(scan);
            scan = next;
        }
    }

/******
 * Free all memory in "freed" chain.
 ******/

    for (i = 0; i < HASH_SIZE; ++i)
    {
        for (scan = MCfreed[i]; scan != NULL; )
        {
            MEMCHAIN *next = scan->m_next;

            free(scan->m_block);
            free(scan);
            scan = next;
        }
    }

    callback("+---------- end of check -----------\n");
}


