#include <stdint.h>
#include "frequencies.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include <errno.h>
#include <string.h>
#include "miniunit.h"
#include "clog.h"


bool calc_frequencies(Frequencies freqs, const char* path, const char** a_error)
{
	bool validFile = false; //initialize the return variable

	FILE* fp = fopen(path, "r");
	
	if (fp == NULL)
	{
		*a_error = strerror(errno);
	}

	else
	{
		for(uchar ch = fgetc(fp); ! feof(fp); ch = fgetc(fp)) 
		{
			freqs[ch] += 1; //adds one to the frequeny of that specific character	
		}
		validFile = true;
		fclose(fp);
	}


		return(validFile);
}

/* vim: set tabstop=4 shiftwidth=4 fileencoding=utf-8 noexpandtab: */
