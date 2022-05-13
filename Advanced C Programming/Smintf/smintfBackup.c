#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include <stdarg.h>
#include "smintf.h"
#include "clog.h"
#include "miniunit.h"

//SINCE FPUTC CAN ONLY BE USED IN ONE LINE OF ONE FUNCTION, WE CREATE A FUNCTION WHOSE ONLY LINE IS FPUTC -> BIG BRAIN LEVEL INFINITE!!~!~!!!!!!!!

char* smintf(const char *format, ...) {

	va_list moreArgs;
	va_start(moreArgs, format);

	//In the two lines below, we first get the size of the input array, seen in sizeInput. Then we
	//allocate memory with malloc using the string size we found and make sure to allocate enough space for the null character
	int sizeInput = _characterCounter(format, moreArgs) + 1; 
	char* finalStringEmpty = malloc(sizeof(*finalStringEmpty) * sizeInput);
	//printf("%d", sizeInput); // this is only so that we don't get an error rn

	//fputs(finalString,stdout);
	char* finalString = _stringCreator(format, finalStringEmpty, moreArgs);

	return(finalString);
	va_end(moreArgs);

}

char* _stringCreator(const char* format, char* finalString, va_list moreArgs) {
	//int decimal;
	int valueToPrint;
	char* valueToPrintChar;
	char valueToPrintActualCharacter;
	int lastIndex;
	int indexFinalString = 0;

	for(int idxInString = 0; format[idxInString] != '\0'; idxInString++) 
	{   
		if (format[idxInString] == '%') 
		{

			if (format[idxInString + 1] == 'c')
			{
				valueToPrintActualCharacter = va_arg(moreArgs, int);
				finalString[indexFinalString] = valueToPrintActualCharacter; 
			}

			else if (format[idxInString + 1] == 's')
			{
				valueToPrintChar = va_arg(moreArgs, char*);
				for(int idxInValueToPrint = 0; valueToPrintChar[idxInValueToPrint] != '\0'; idxInValueToPrint++) 
				{
					//fputc(valueToPrintChar[idxInValueToPrint], stdout);
					//
					//Here the code takes into account the length of the string and updates accordingly
					finalString[indexFinalString] = valueToPrintChar[idxInValueToPrint]; 
					indexFinalString++;
				}
			}

			else if (format[idxInString + 1] == 'd')
			{
				valueToPrint = va_arg(moreArgs, int);

				//print_integer(10, valueToPrint, "");
			}

			else if (format[idxInString + 1] == 'b')
			{
				valueToPrint = va_arg(moreArgs, int);

				//print_integer(2, valueToPrint, "0b");
			}

			else if (format[idxInString + 1] == 'x')
			{
				valueToPrint = va_arg(moreArgs, int);

				//print_integer(16, valueToPrint, "0x");
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
					//fputc('-', stdout);
					finalString[indexFinalString] = '-';
				}

				//fputc('$', stdout);
				finalString[indexFinalString] = '$';


				//decimal = abs(valueToPrint % 100);
				//valueToPrint = abs(valueToPrint / 100);

				//print_integer(10, valueToPrint, "");            

				//fputc('.', stdout);
				//fputc((decimal / 10) + '0', stdout);
				//fputc((decimal % 10) + '0', stdout); 
				finalString[indexFinalString] = '.';

				//finalString[idxInString + 1] = char* (decimal / 10);
				//finalString[idxInString + 2] = char* (decimal % 10);
			}

			else
			{
				finalString[indexFinalString] = '%';

				finalString[indexFinalString + 1] = format[idxInString + 1];  
			}

			idxInString += 1;

			
		}

		else 
		{
			//fputc(format[idxInString], stdout);
			finalString[indexFinalString] = format[idxInString];
			//fputc('=', stdout);
			
			//fputc('\n',stdout);
			//fputc(finalString[idxInString], stdout);
		}
		indexFinalString++;

		lastIndex =indexFinalString;
	}

	//va_end(moreArgs);  
	finalString[lastIndex] = '\0';
	/*
	printf("Last index: %d Index final String: %d", lastIndex, indexFinalString);
	fputc('\n', stdout);
	fputc(finalString[0], stdout);
	fputc('-', stdout);
	fputc(finalString[1],stdout);
	fputc('-',stdout);
	fputc(finalString[2], stdout);
	fputc('-',stdout);
	fputc(finalString[3], stdout);
	fputc('-',stdout);
	fputc(finalString[4], stdout);
	*/





	return(finalString);
}

int _characterCounter(const char *format, ...) {

	int valueToPrint;
	char* valueToPrintChar;

	int charCounter = 0; //We are reusing our original mintf function to create a character counter so that
						 //we know how many characters the final string will have. By knowing the amount of characters
						 //in the final string, we can then use that to allocate the necessary memory with MALLOC. The logic
						 //behind this counter is to start with zero and add one everytime we were supposed print in the original 
						 //function so that we know the actual amount of characters. 
	
	va_list moreArgs;
	va_start(moreArgs, format);  


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

	va_end(moreArgs);   

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
