#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include "mintf.h"

int main(int argc, char* argv[]) {
	//Test 00: empty test
	////Expect: ""
	
	//Test 01: Empty string
	mintf("");
	fputc('\n', stdout);
	//Expect: ""
	
	//Test 02: string with single char
	mintf("M");
	fputc('\n', stdout);
	//Expect: "M"
	
	//Test 03: string containing any number of chars
	mintf("Neymar");
	fputc('\n', stdout);
	//Expect: "Neymar"
	
	//Test 04: test printing "%%"
	mintf("%%");
	fputc('\n',stdout);
	//Expect: "%"
	
	//Test 05: test single digit numbers
	mintf("%d", 7);
	fputc('\n',stdout);
	//Expect: 7
	
	//Test 06: test multi digit numbers
	mintf("%d", 6969);
	fputc('\n',stdout);
	//Expect: 6969
	
	//Test 07: test negative single digit numbers
	mintf("%d", -7);
	fputc('\n',stdout);
	//Expect: -7
	
	//Test 08: test negative multi digit numbers
	mintf("%d", -6969);
	fputc('\n',stdout);
	//Expect: -6969

	//Test 09: test single character from ASCII using numbers
	mintf("%c", 77);
	fputc('\n',stdout);
	//Expect: "M"
	
	//Test 10: print a character using a character as argument
	mintf("%c", 'M');
	fputc('\n',stdout);
	//Expect: M
	
	//Test 11: printing string
	mintf("My name is %s", "Miguel");
	fputc('\n',stdout);
	//Expect: "My name is Miguel")

	//Test 12: test printing positive numbers in binary
	mintf("%b", 15);
	fputc('\n',stdout);
	//Expect: 0b1111
	
	//Test 13: test negative numbers in binary
	mintf("%b", -15);
	fputc('\n',stdout);
	//Expect: -0b1111
	
	//Test 14: Printing positive hexadecimal numbers
	mintf("%x", 256);
	fputc('\n',stdout);
	//Expect: 0x100
	
	//Test 15: Printing negative hex numbers
	mintf("%x", -256);
	fputc('\n',stdout);
	//Expect: -0x100
	
	//Test 16: Printing currency
	mintf("%$", 6969);
	fputc('\n',stdout);
	//Expect: "$69.69)"
	
	//Test 17: Test them all together:
	mintf("Decimal: %d Binary: %b Hexadecimal: %x Percentage: %% Money: %$ Character: %c String: %s", 163, 8, 16, 1573, 'M', "TANTANTAN");
	fputc('\n',stdout);
	//Expect: "Decimal: 163 Binary: 0b1000 Hexadecimal: 0x10 Percentage: % Money: $15.73 Character: M String: TANTANTAN"	
	
	//Test 18: Test negative cents
	mintf("Negative cents: %$", -99);
	fputc('\n', stdout);
	//Expect: Negative cents: -$0.99
	
	//Test 19: test using a single percentage
	mintf("I sold 92% of my oranges");
	fputc('\n',stdout);

	return EXIT_SUCCESS;
}
/* vim: set tabstop=4 shiftwidth=4 fileencoding=utf-8 noexpandtab: */
