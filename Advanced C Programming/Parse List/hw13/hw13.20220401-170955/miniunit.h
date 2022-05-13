#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include <stdio.h>
#include "clog.h"
#include <string.h>

#ifndef __MINIUNIT_H__
#define __MINIUNIT_H__

#define mu_start() int __mu_LineNumberFailure = 0

#define mu_check(condition) \
	do{\
	  	 \
		if (!(condition) && (__mu_LineNumberFailure == 0))\
		{ \
			__mu_LineNumberFailure = __LINE__; \
		} \
	} while(false)

#define mu_run(function) \
	do {\
		int functionOutput = function(); \
		\
		if (functionOutput == 0) \
		{ \
			logf_green("Test passed: %s\n", (#function)); \
		} \
\
		else \
		{ \
			logf_red("Test failed: %s at line %d\n", (#function), functionOutput); \
		} \
	 } while(false) 

#define mu_end() return __mu_LineNumberFailure 

#define mu_check_strings_equal(s1, s2) mu_check(strcmp((s1),(s2)) == 0)



#endif /* end of include guard: __MINIUNIT_H__ */
