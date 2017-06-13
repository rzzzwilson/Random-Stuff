#ifndef MEMCHECK_H
#define MEMCHECK_H

/******************************************************************************\
 *                           M E M C H E C K . H                              *
 *                          =====================                             *
 *                                                                            *
 *   Include file for the memcheck system. See memcheck.c for details.        *
 *                                                                            *
\******************************************************************************/

#include <stdarg.h>

#if defined(MCDEBUG)
    #define malloc(a)		(MCmalloc(__FILE__,__LINE__,a))
    #define calloc(a,b)		(MCcalloc(__FILE__,__LINE__,a,b))
    #define realloc(a,b)	(MCrealloc(__FILE__,__LINE__,a,b))
    #define free(a)		    (MCfree(__FILE__,__LINE__,a))

    #define CHECKSIZE	8

    #define MC_VERBOSE	1

    typedef void CALLBACK(char *fmt, ...);

    void  MCinit(unsigned, CALLBACK *cback);
    void *MCmalloc(char *file, unsigned line, unsigned size);
    void  MCfree(char *file, unsigned line, void *block);
    void *MCcalloc(char *file, unsigned line, unsigned num, unsigned size);
    void *MCrealloc(char *file, unsigned line, void *addr, unsigned size);
    void  MCcheck(void);
    void  MCterm(void);
#else
    #define MCinit(a,b);	;
    #define MCcheck();		;
    #define MCterm();		;
#endif


#endif
