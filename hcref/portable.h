/******************************************************************************\
 *                            P O R T A B L E . H                             *
 *                           =====================                            *
 *                                                                            *
 *                                                                            *
\******************************************************************************/

#ifndef PORTABLE_H
#define PORTABLE_H

#include <stdio.h>
#include <stdarg.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <ctype.h>

#define VERSION		0
#define RELEASE		2

#define DATE		"5 July, 2000"


typedef int     bool;

#ifndef __BORLANDC__
#   define max(a,b)     ((a>b) ? (a) : (b))
#endif

#define TRUE            1
#define FALSE           0

#define MIN_LINE	10

#define FILENAME_LEN    256
#define TOKBUFF_LEN     256
#define BUFF_SIZE       512

#define MAX_KEYS        43

#define DEF_TOPMARGIN   5
#define DEF_LEFTMARGIN  5

#define new(a)          (a *) malloc(sizeof(a))

#ifdef __BORLANDC__
#   define Ustrcmp      strcmpi
#else
#   define Ustrcmp      strcasecmp
#endif


#endif

