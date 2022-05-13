#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>
#include <stdbool.h>
#include <stdarg.h>
#include "mintf.h"

void print_integer (int radix, int n, char* s);
void mintf(const char* format, ...);

void mintf(const char* format, ...) {

	int decimal;
	int valueToPrint;
	char* valueToPrintChar;

	va_list moreArgs; 
	va_start(moreArgs, format);  


	for(int idxInString = 0; format[idxInString] != '\0'; idxInString++) 
	{   
		if (format[idxInString] == '%') 
		{

			if (format[idxInString + 1] == 'c')
			{
				valueToPrint = va_arg(moreArgs, int);

				fputc(valueToPrint, stdout);
			}

			else if (format[idxInString + 1] == 's')
			{
				valueToPrintChar = va_arg(moreArgs, char*);
				for(int idxInValueToPrint = 0; valueToPrintChar[idxInValueToPrint] != '\0'; idxInValueToPrint++) 
				{
					fputc(valueToPrintChar[idxInValueToPrint], stdout);
				}
			}

			else if (format[idxInString + 1] == 'd')
			{
				valueToPrint = va_arg(moreArgs, int);

				print_integer(10, valueToPrint, "");
			}

			else if (format[idxInString + 1] == 'b')
			{
				valueToPrint = va_arg(moreArgs, int);

				print_integer(2, valueToPrint, "0b");
			}

			else if (format[idxInString + 1] == 'x')
			{
				valueToPrint = va_arg(moreArgs, int);

				print_integer(16, valueToPrint, "0x");
			}

			else if (format[idxInString + 1] == '%')
			{
				fputc('%', stdout);
			}

			else if(format[idxInString + 1] == '$')
			{ 
				valueToPrint = va_arg(moreArgs, int);


				if (valueToPrint < 0)
				{

					fputc('-', stdout);
				}

				fputc('$', stdout);

				decimal = abs(valueToPrint % 100);
				valueToPrint = abs(valueToPrint / 100);

				print_integer(10, valueToPrint, "");            

				fputc('.', stdout);
				fputc((decimal / 10) + '0', stdout);
				fputc((decimal % 10) + '0', stdout); 

			}

			else
			{
				fputc('%', stdout);
				fputc(format[idxInString + 1], stdout);
			}

			idxInString += 1;

		}

		else 
		{
			fputc(format[idxInString], stdout);
		}
	}

	va_end(moreArgs);   
}

void print_integer (int radix, int n, char* s) {

	int numberSystem = radix;
	int controlVariable = -1; 
	int remainder; 
	int divider; 
	unsigned int decimalNumCopy = n;
	unsigned int decimalNumber = n;
	unsigned int currentDecNum;

	if (n < 0) {
		fputc('-', stdout);
		decimalNumCopy = -n;
		decimalNumber = -n;

	}

	for(int idxInStr = 0; s[idxInStr] != '\0'; idxInStr++) {
		fputc(s[idxInStr], stdout);
	}

	while (decimalNumCopy != 0) 
	{
		remainder = decimalNumCopy % numberSystem;
		decimalNumCopy = decimalNumCopy / numberSystem;

		controlVariable++; 
	} 

	while (controlVariable >= 0) 
	{
		divider = 1;

		if (controlVariable == 0)
		{ 
			divider = 1;
		}
		else
		{
			for (int i = controlVariable; i > 0; i--)
			{
				divider *= numberSystem;
			}
		}

		currentDecNum = decimalNumber / divider; 
		remainder = currentDecNum % numberSystem; 

		if (remainder > 9) {
			fputc(remainder + 'W', stdout);

		}

		else {
			fputc('0' + remainder, stdout);
		}

		controlVariable--;
	}

	if (decimalNumber == 0) {
		fputc('0', stdout);   
	}          
}
