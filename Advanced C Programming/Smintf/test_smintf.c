#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include <stdarg.h>
#include <string.h>
#include "smintf.h"
#include "clog.h"
#include "miniunit.h"

#define mu_check_smintf(expected,...)\
	do { \
		char* actual = smintf(__VA_ARGS__); \
		mu_check_strings_equal((expected), (actual)); \
		free(actual); \
	} while(false) \


//we find the correct length for any kind of input. In this testing set, we will test the 
//_characterCounter helper function to make sure it works as desired.

int _testSmintfNoArguments() {
	mu_start();
	mu_check_strings_equal("", "");
	mu_check_smintf("The sky is blue", "The sky is blue");
	mu_check_smintf("ABC", "ABC");
	mu_check_smintf("This homework is tough", "This homework is tough");
	mu_end();

}

int _testSmintfIntegers() {
	mu_start();
	mu_check_smintf("10","%d", 10);
	mu_check_smintf("Number 572 with words", "Number %d with words", 572);
	mu_check_smintf("-6", "%d", -6);
	mu_check_smintf("0", "%d", 0);
	mu_check_smintf("Number 1 and Number -2", "Number %d and Number %d", 1,-2);
	mu_check_smintf("I ate 92% of the apples", "I ate %d% of the apples", 92);
	mu_end();

}

int _testSmintfBinary() {
	mu_start();
	mu_check_smintf("0b1111", "%b", 15);
	mu_check_smintf("-0b1111","%b", -15);
	mu_check_smintf("Binary 0b10000!","Binary %b!", 16); 
	mu_end();
}

int _testSmintfHex() {
	mu_start();
	mu_check_smintf("0x10", "%x", 16);
	mu_check_smintf("-0x10", "%x", -16);
	mu_check_smintf("Hex 0x100!","Hex %x!", 256); 
	mu_end();
}

int _testSmintfCharacters() {
	mu_start();
	mu_check_smintf("M", "%c", 77);
	mu_check_smintf("Try printing the letter A", "Try printing the letter %c", 65);
	mu_check_smintf("M and N", "%c and %c",'M', 'N');
	mu_end();
}

int _testSmintfStrings() {
	mu_start();
	mu_check_smintf("Hello", "%s", "Hello");
	mu_check_smintf("Hail Purdue!", "Hail %s!", "Purdue");
	mu_check_smintf("String1 and String2?", "%s and %s?", "String1", "String2");
	mu_end();
}

int _testSmintfPercentages() {
	mu_start();
	mu_check_smintf("%", "%");
	mu_check_smintf("length %!", "length %!");
	mu_check_smintf("%", "%%");
	mu_end();
}

int _testSmintfMoney() {
	mu_start();
	mu_check_smintf("$69.69","%$", 6969);
	mu_check_smintf("Negative cents: -$0.99!", "Negative cents: %$!", -99);
	mu_check_smintf("Brandon is a 10!", "%s is a %d!", "Brandon", 10);
	mu_end();

}

int main(int argc, char* argv[]) {
	mu_run(_testSmintfNoArguments);
	mu_run(_testSmintfCharacters);
	mu_run(_testSmintfPercentages);
	mu_run(_testSmintfStrings);
	mu_run(_testSmintfIntegers);
	mu_run(_testSmintfBinary);
	mu_run(_testSmintfHex);
	mu_run(_testSmintfMoney);
	return EXIT_SUCCESS;
}
/* vim: set tabstop=4 shiftwidth=4 fileencoding=utf-8 noexpandtab: */
