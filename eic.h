/* eic.h
 *
 *	(C) Copyright May  7 1995, Edmond J. Breen.
 *		   ALL RIGHTS RESERVED.
 * This code may be copied for personal, non-profit use only.
 * Modified for PLD GNU/Linux by a.miskiewicz@opengroup.org
 */
#ifndef EICH_
#define EICH_

#include <sys/types.h>

int EiC_run(int, char**);
void EiC_init_EiC(void);
void EiC_switches(char *);
void EiC_parseString(char * command,...);
void EiC_setMessageDisplay(void (*)(char *));

#endif /* EICH_ */














