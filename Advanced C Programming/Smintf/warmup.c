 /* vim: set tabstop=4 shiftwidth=4 fileencoding=utf-8 noexpandtab: */
#include <stdio.h>
#include <stdlib.h>


char* my_strdup(const char* original) {
	int charCounter = 0;

	//in the below loop I find the number of characters in the input string
	for (int idxins = 0; original[idxins] != '\0'; idxins++) {
		charCounter++;
	}
	
	charCounter++; //This is to allocate enough space for the null character

	//here I allocate a memory block to the charCopy variable based on the numbr of character we have in the original string
	char* charCopy = malloc(sizeof(*charCopy) * charCounter);
	
	for (int idxOriginal = 0; idxOriginal < charCounter; idxOriginal++) {
		charCopy[idxOriginal] = original[idxOriginal];
	}
	
	/*
	do {
		charCopy[idxOriginal] = original[idxOriginal];
		idxOriginal++;
	} while (idxOriginal < charCounter); */


	return(charCopy);
}

int main(int argc, char *argv[]) {
	char s[] = "abc\n";
	fputs(s, stdout);  // Should print "abc" followed by a newline ('\n')

	char* t = my_strdup(s);
	fputs(t, stdout);  // Should print "abc" followed by a newline ('\n')
	free(t);

	return EXIT_SUCCESS;
}
