/******************************************************************************\
 *                                 E R R O R . C                              *
 *                                ===============                             *
 *                                                                            *
 *      This file contains the error routines for the hcref program.          *
 *                                                                            *
\******************************************************************************/

#include "portable.h"

#include "error.h"

/*******************************************************************************
       Name :
Description :
 Parameters :
    Returns :
   Comments :
*******************************************************************************/
void
error(char *fmt, ...)
{
    va_list    ap;

    va_start(ap, fmt);
    vfprintf(stdout, fmt, ap);
    va_end(ap);

    fprintf(stdout, "\n");

    exit(RET_ERROR);
}
