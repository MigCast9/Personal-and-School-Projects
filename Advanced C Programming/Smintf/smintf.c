#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include <stdarg.h>
#include "smintf.h"
#include "clog.h"
#include "miniunit.h"

int _printInteger (int radix, int n, char* s);
int _characterCounter(const char *format, va_list moreArgs);
char* _stringCreator(const char *format, char* finalString, va_list moreArgs);
char* _numberDealer(char *unfinishedString,int  *indexFinalStringCopy,int indexFinalString, int radix, int n, char *s);


char* smintf(const char *format, ...) {

	va_list moreArgs;
	va_start(moreArgs, format);
	va_list moreArgsCopy;
	va_copy(moreArgsCopy, moreArgs);

	//allocate memory with malloc using the string size we found and make sure to allocate enough space for the null character
	int sizeInput = _characterCounter(format, moreArgs) + 1; 
	char* finalStringEmpty = malloc(sizeof(*finalStringEmpty) * sizeInput);
	char* finalString = _stringCreator(format, finalStringEmpty, moreArgsCopy);

	return(finalString);
	va_end(moreArgs);
	va_end(moreArgsCopy);

}

char* _stringCreator(const char* format, char* finalString, va_list moreArgs) {
	int decimal;
	int valueToPrint;
	char* valueToPrintChar;
	int indexFinalString = 0; //index of the final string. We will update the returned string according to this variable
	int indexFinalStringCopy;


	for(int idxInString = 0; format[idxInString] != '\0'; idxInString++) 
	{   
		if (format[idxInString] == '%') 
		{

			if (format[idxInString + 1] == 'c')
			{
				valueToPrint = va_arg(moreArgs,int);
				finalString[indexFinalString] = valueToPrint;
			}

			else if (format[idxInString + 1] == 's')
			{
				valueToPrintChar = va_arg(moreArgs, char*);
				for(int idxInValueToPrint = 0; valueToPrintChar[idxInValueToPrint] != '\0'; idxInValueToPrint++) 
				{
					finalString[indexFinalString] = valueToPrintChar[idxInValueToPrint];
					indexFinalString++;
				}
				indexFinalString--;
				//free(valueToPrintChar);
			}

			else if (format[idxInString + 1] == 'd')
			{
				valueToPrint = va_arg(moreArgs, int);
				finalString = _numberDealer(finalString,&indexFinalStringCopy,indexFinalString, 10, valueToPrint, "");
				indexFinalString = indexFinalStringCopy - 1;
			}

			else if (format[idxInString + 1] == 'b')
			{
				valueToPrint = va_arg(moreArgs, int);
				finalString = _numberDealer(finalString,&indexFinalStringCopy,indexFinalString, 2, valueToPrint, "0b");
				indexFinalString = indexFinalStringCopy - 1;
			}

			else if (format[idxInString + 1] == 'x')
			{
				valueToPrint = va_arg(moreArgs, int);
				finalString = _numberDealer(finalString,&indexFinalStringCopy,indexFinalString, 16, valueToPrint, "0x");
				indexFinalString = indexFinalStringCopy - 1;

			}

			else if (format[idxInString + 1] == '%')
			{
				finalString[indexFinalString] = '%';
			}

			else if(format[idxInString + 1] == '$')
			{ 
				valueToPrint = va_arg(moreArgs, int);


				if (valueToPrint < 0)
				{
					finalString[indexFinalString] = '-';
					indexFinalString++;
				}

				finalString[indexFinalString] = '$';
				indexFinalString++;

				decimal = abs(valueToPrint % 100);
				valueToPrint = abs(valueToPrint / 100);

				finalString = _numberDealer(finalString, &indexFinalStringCopy,indexFinalString, 10, valueToPrint, "");
				indexFinalString = indexFinalStringCopy;


				finalString[indexFinalString] = '.';
				
				indexFinalString++;
				finalString[indexFinalString] = decimal / 10 + '0';

				indexFinalString++;
				finalString[indexFinalString] = decimal % 10 + '0';
			}

			else
			{
				finalString[indexFinalString] = '%';
				indexFinalString++;
				finalString[indexFinalString] = format[idxInString + 1]; 	
			}

			idxInString += 1;

		}

		else 
		{
			finalString[indexFinalString] = format[idxInString];
		}

		indexFinalString++;
	}
	
	finalString[indexFinalString] = '\0';

	return(finalString);
}

char* _numberDealer(char *unfinishedString,int  *indexFinalStringCopy,int indexFinalString,int radix, int n, char *s) {	
	
	int numberSystem = radix;
	int controlVariable = -1; 
	int remainder; 
	int divider; 
	unsigned int decimalNumCopy = n;
	unsigned int decimalNumber = n;
	unsigned int currentDecNum;

	if (n < 0) {
		unfinishedString[indexFinalString] = '-';
		decimalNumCopy = -n;
		decimalNumber = -n;
		indexFinalString++;

	}

	for(int idxInStr = 0; s[idxInStr] != '\0'; idxInStr++) {
		unfinishedString[indexFinalString] = s[idxInStr];
		indexFinalString++;
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
			unfinishedString[indexFinalString] = remainder + 'W';
		}

		else {
			unfinishedString[indexFinalString] = '0' + remainder;
			//fputc('0' + remainder, stdout);
		}
		
		indexFinalString++;
		controlVariable--;
	}

	if (decimalNumber == 0) {
		unfinishedString[indexFinalString] = '0';
		//fputc('0', stdout);   
		indexFinalString++;
	}          
	
	*indexFinalStringCopy = indexFinalString;
	return(unfinishedString);
}


int _characterCounter(const char *format, va_list moreArgs) {

	int valueToPrint;
	char* valueToPrintChar;

	int charCounter = 0; //We are reusing our original mintf function to create a character counter so that
						 //we know how many characters the final string will have. By knowing the amount of characters
						 //in the final string, we can then use that to allocate the necessary memory with MALLOC. The logic
						 //behind this counter is to start with zero and add one everytime we were supposed print in the original 
						 //function so that we know the actual amount of characters. 
	
	//va_list moreArgs;
	//va_start(moreArgs, format);  


	for(int idxInString = 0; format[idxInString] != '\0'; idxInString++)		 
	{   
		if (format[idxInString] == '%') 
		{

			if (format[idxInString + 1] == 'c')
			{
				valueToPrint = va_arg(moreArgs, int);

				charCounter++;
			}

			else if (format[idxInString + 1] == 's')
			{
				valueToPrintChar = va_arg(moreArgs, char*);
				for(int idxInValueToPrint = 0; valueToPrintChar[idxInValueToPrint] != '\0'; idxInValueToPrint++) 
				{
					charCounter++;
				}
			}

			else if (format[idxInString + 1] == 'd')
			{
				valueToPrint = va_arg(moreArgs, int);

				charCounter +=  _printInteger(10, valueToPrint, "");
			}

			else if (format[idxInString + 1] == 'b')
			{
				valueToPrint = va_arg(moreArgs, int);

				charCounter += _printInteger(2, valueToPrint, "0b");
			}

			else if (format[idxInString + 1] == 'x')
			{
				valueToPrint = va_arg(moreArgs, int);

				charCounter += _printInteger(16, valueToPrint, "0x");
			}

			else if (format[idxInString + 1] == '%')
			{
				charCounter++;
			}

			else if(format[idxInString + 1] == '$')
			{ 
				valueToPrint = va_arg(moreArgs, int);


				if (valueToPrint < 0)
				{
					charCounter++;
				}
				
				valueToPrint = abs(valueToPrint / 100);


				charCounter += _printInteger(10, valueToPrint, "");

				charCounter += 4;

			}

			else
			{
				charCounter += 2;
			}

			idxInString += 1;

		}

		else 
		{
			charCounter++;
		}
	}

	//va_end(moreArgs);   

	return(charCounter);
}


int _printInteger (int radix, int n, char* s) {

	int numberSystem = radix;
	int controlVariable = -1; 
	int remainder; 
	int divider; 
	unsigned int decimalNumCopy = n;
	unsigned int decimalNumber = n;
	unsigned int currentDecNum;
	int charCounter = 0;

	if (n < 0) {
		//fputc('-', stdout);
		charCounter++;
		decimalNumCopy = -n;
		decimalNumber = -n;

	}

	for(int idxInStr = 0; s[idxInStr] != '\0'; idxInStr++) {
		//fputc(s[idxInStr], stdout);
		charCounter++;
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
			//fputc(remainder + 'W', stdout);
			charCounter++;
		}

		else {
			//fputc('0' + remainder, stdout);
			charCounter++;
		}

		controlVariable--;
	}

	if (decimalNumber == 0) {
		//fputc('0', stdout);   
		charCounter++;
	}     

	return(charCounter);
}
/*
int main(int argc, char* argv[]) {
	
	return EXIT_SUCCESS;
}*/
/* vim: set tabstop=4 shiftwidth=4 fileencoding=utf-8 noexpandtab: */
