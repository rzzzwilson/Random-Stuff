/******************************************************************************\
 *                                 L I S T . H                                *
 *                                =============                               *
 *                                                                            *
 *                                                                            *
\******************************************************************************/

#ifndef LIST_H
#define LIST_H

void list_open(char *cdir, int pwidth);
void list_add(char *token, char *fname, int lnum, bool defn);
void list_menuhtml(FILE *out, char *outputdir);
void list_cref(void);
void list_tokenlist(void);
void list_close(void);

#endif

