/******************************************************************************\
 *                               S C A N N E R . H                            *
 *                              ===================                           *
 *                                                                            *
 *                                                                            *
\******************************************************************************/

#ifndef SCANNER_H
#define SCANNER_H

void  scan_open(char *infile, char *outfile, char *cdir);
char *scan_token(int *lnum, bool *defn);
void  scan_emit(bool html);
void  scan_close(void);


#endif


