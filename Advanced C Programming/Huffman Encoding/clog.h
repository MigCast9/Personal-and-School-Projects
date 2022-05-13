#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include <stdio.h>

#ifndef NDEBUG //If the NDEBUG symbol isnt present it will read until the ELSE statement

#ifndef __CLOG_H__
#define __CLOG_H__
#endif

//Here we define the macros we use
#define logf_ printf

#define __mu_logf_any_color(ansiColor ,...) \
	do {					\
		if (isatty(STDOUT_FILENO) == true)			\
		{						\
			printf("%s",ansiColor); \
		}						\
								\
		logf_(__VA_ARGS__); 	\
								\
		if (isatty(STDOUT_FILENO) == true)			\
		{						\
			printf("\x1b[0m");  \
		}						\
	} while(false)

#define logf_red(...) __mu_logf_any_color("\x1b[31m", __VA_ARGS__)
#define logf_green(...) __mu_logf_any_color("\x1b[32m", __VA_ARGS__)
#define logf_yellow(...) __mu_logf_any_color("\x1b[33m", __VA_ARGS__)
#define logf_blue(...) __mu_logf_any_color("\x1b[34m", __VA_ARGS__)
#define logf_magenta(...) __mu_logf_any_color("\x1b[35m", __VA_ARGS__)
#define logf_cyan(...) __mu_logf_any_color("\x1b[36m", __VA_ARGS__)

#define log_int(n) printf("%s == %d\n", (#n), (n))

#define log_char(c) printf("%s == '%c'\n", (#c), (c))

#define log_str(str) printf("%s == \"%s\"\n", (#str), (str))

#define log_addr(var) printf("%s == %p\n", (#var), (void*) var)

#define log_float(n) printf("%s == %.016f\n", (#n), (n))

#define log_bool(b) printf("%s == %s\n", (#b), (b ? "true" : "false"))

#else
#define logf_(...) 
#define logf_red(...) 
#define logf_yellow(...) 
#define logf_green(...) 
#define logf_blue(...) 
#define logf_magenta(...) 
#define logf_cyan(...) 
#define log_int(...)
#define log_char(...)
#define log_str(...)
#define log_addr(...)
#define log_float(...)
#define log_bool(...)




#endif /* end of include guard: __CLOG_H__ */
