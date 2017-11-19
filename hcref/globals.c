/******************************************************************************\
 *                               G L O B A L S . C                            *
 *                              ===================                           *
 *                                                                            *
 *                                                                            *
\******************************************************************************/

#include "portable.h"

#include "globals.h"

int   braces;
int   parentheses;
bool  numbertokens;
char  dirdelim;

char *key_table[MAX_KEYS];

char  timebuff[128];


/*******************************************************************************
       Name :
Description :
 Parameters :
    Returns :
   Comments :
*******************************************************************************/
void
globals_init(void)
{
    braces = 0;
    parentheses = 0;
    numbertokens = FALSE;
#ifdef __BORLANDC__
    dirdelim = '\\';
#else
    dirdelim = '/';
#endif
}
