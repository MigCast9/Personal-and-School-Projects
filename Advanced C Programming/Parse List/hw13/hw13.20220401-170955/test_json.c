#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include "json.h"
#include "miniunit.h"
#include <string.h>

int _test_parse_int_valid() {
	mu_start();
	int result1;
	const char* input1 = "0"; // address of the first character, '0'
	const char* pos1 = input1; //will be the address of the character to look at next
	bool is_success1 = parse_int(&result1, &pos1);
	//printf("%d", result);
	mu_check(is_success1);   // because the input is valid
	mu_check(result1 == 0);
	mu_check(pos1 == input1 + 1);
	
	mu_end();
}

int _test_parse_integer() {
	mu_start();
	int result2;
	const char* input2 = "124"; // address of the first character, '0'
	const char* pos2 = input2; //will be the address of the character to look at next
	bool is_success2 = parse_int(&result2, &pos2);
	mu_check(is_success2);   // because the input is valid
//	printf("%d", result2);
	mu_check(result2 == 124);
	mu_check(pos2 == input2 + 3);
	
	mu_end();
}

int _test_parse_int_invalid() {
	mu_start();
	int   result3;  // will be initialized in parse_int(…)
	const char* input3 = "A";
	const char* pos3 = input3;
	bool is_success3 = parse_int(&result3, &pos3);
	mu_check(!is_success3);  // because the input is invalid 
	mu_check(pos3 == input3); // failure should be at the first character in the input
	mu_end();
}

int _test_parse_int_negativeInvalid() {
	mu_start();
	int   result4;  // will be initialized in parse_int(…)
	const char* input4 = "-A";
	const char* pos4 = input4;
	bool is_success4 = parse_int(&result4, &pos4);
	mu_check(!is_success4);  // because the input is invalid 
	mu_check(pos4 == input4 + 1); // failure should be at the first character in the input
	mu_end();
}


int _test_parse_int_negative() {
	mu_start();
	int result5;
	const char* input5 = "-123"; // address of the first character, '0'
	const char* pos5 = input5; //will be the address of the character to look at next
	bool is_success5 = parse_int(&result5, &pos5);
	//printf("%d", result);
	mu_check(is_success5);   // because the input is valid
	mu_check(result5 == -123);
	mu_check(pos5 == input5 + 4);
	
	mu_end();
}

int _test_parse_int_withBreak() {
	mu_start();
	int result6;
	const char* input6 = "123AAA"; // address of the first character, '0'
	const char* pos6 = input6; //will be the address of the character to look at next
	bool is_success6 = parse_int(&result6, &pos6);
	//printf("%d", result);
	mu_check(is_success6);   // because the input is valid
	mu_check(result6 == 123);
	mu_check(pos6 == input6 + 3);
	
	mu_end();
}

int _test_parse_int_negativeWithBreak() {
	mu_start();
	int result7;
	const char* input7 = "-123AAA"; // address of the first character, '0'
	const char* pos7 = input7; //will be the address of the character to look at next
	bool is_success7 = parse_int(&result7, &pos7);
	//printf("%d", result);
	mu_check(is_success7);   // because the input is valid
	mu_check(result7 == -123);
	mu_check(pos7 == input7 + 4);
	
	mu_end();
}



static int _test_parse_string_valid_empty() {
	
	mu_start();
	char* result;
	char const* input = "\"\"";
	char const* pos = input;
	bool is_success = parse_string(&result, &pos);
	mu_check(is_success);
	mu_check_strings_equal("", result);
	mu_check(pos == input + 2);
	mu_check(*pos == '\0');
	free(result);

	mu_end();
}
static int _test_parse_string_valid_one_char() {

	mu_start();

	char* result;
	char const* input = "\"A\"";
	char const* pos = input;
	bool is_success = parse_string(&result, &pos);
	mu_check(is_success);
	mu_check_strings_equal("A", result);
	mu_check(pos == input + 3);
	mu_check(*pos == '\0');
	free(result);

	mu_end();
}


static int _test_parse_string_invalid() {
	mu_start();

	char* result;
	char const* input = "\"A";
	char const* pos = input;
	bool is_success = parse_string(&result, &pos);
	mu_check(!is_success);
	mu_check(pos == input + 2);
	mu_check(*pos == '\0');

	mu_end();
}

static int _test_parse_string_invalid2() {
	mu_start();

	char* result;
	char const* input = "ABC\"";
	char const* pos = input;
	bool is_success = parse_string(&result, &pos);
	mu_check(!is_success);
	mu_check(pos == input);
	mu_check(*pos == 'A'); //SHOULD BE A

	mu_end();
}

static int _test_parse_string_invalid3() {
	mu_start();

	char* result;
	char const* input = "\"A\nB\"";
	char const* pos = input;
	bool is_success = parse_string(&result, &pos);
	mu_check(!is_success);
	mu_check(pos == input + 2);
	mu_check(*pos == '\n');

	mu_end();
}

static int _test_parse_string_invalid4() {
	mu_start();

	char* result;
	char const* input = "ABC";
	char const* pos = input;
	bool is_success = parse_string(&result, &pos);
	mu_check(!is_success);
	mu_check(pos == input);
	mu_check(*pos == 'A');

	mu_end();
}

static int _test_parse_string_valid_multiple_chars() {
	mu_start();

	char* result;
	char const* input = "\"ABC\"";
	char const* pos = input;
	bool is_success = parse_string(&result, &pos);
	mu_check(is_success);
	mu_check_strings_equal("ABC", result);
	mu_check(pos == input + 5);
	mu_check(*pos == '\0');

	free(result);

	mu_end();
}

static int _test_parse_string_valid_complicated() {
	mu_start();

	char* result;
	char const* input = "\"ABC\"ABC";
	char const* pos = input;
	bool is_success = parse_string(&result, &pos);
	mu_check(is_success);
	mu_check_strings_equal("ABC", result);
	mu_check(pos == input + 5);
	mu_check(*pos == 'A');

	free(result);

	mu_end();
}



static int _test_parse_element_empty_invalid() {
	mu_start();

	Element element;
	char const* input = "";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(!is_success);
	mu_check(*pos == '\0');
	mu_check(pos == input);

	input = "\"";
	pos = input;
	is_success = parse_element(&element, &pos);
	mu_check(!is_success);
	mu_check(*pos == '\0');
	mu_check(pos == input + 1);

	mu_end();
}

static int _test_parse_element_int_plain() {
	mu_start();

	Element element;
	char const* input = "1";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.as_int == 1);
	mu_check(element.type == ELEMENT_INT);
	mu_check(pos == input + 1);
	mu_check(*pos == '\0');
	
	//negative number
	input = "-2";
	pos = input;
	is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.as_int == -2);
	mu_check(element.type == ELEMENT_INT);
	mu_check(pos == input + 2);
	mu_check(*pos == '\0');

	input = "12";
	pos = input;
	is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.as_int == 12);
	mu_check(element.type == ELEMENT_INT);
	mu_check(pos == input + 2);
	mu_check(*pos == '\0');

	mu_end();
}

static int _test_parse_element_with_leading_whitespace() {
	mu_start();

	Element element;
	char const* input = "  1";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.as_int == 1);
	mu_check(element.type == ELEMENT_INT);
	mu_check(pos == input + 3);
	mu_check(*pos == '\0');

	mu_end();

}

static int _test_parse_element_int_oddballs() {
	mu_start();

	Element element;
	char const* input = " 4 A";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.as_int == 4);
	mu_check(element.type == ELEMENT_INT);
	mu_check(pos == input + 2);
	mu_check(*pos == ' ');

	mu_end();
}

static int _test_parse_element_invalid() {
	mu_start();

	Element element;
	char const* input = "--4";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(!is_success);
	mu_check(pos == input + 1);
	mu_check(*pos == '-');

	mu_end();
}

static int _test_parse_element_string() {
	mu_start();

	Element element;
	char const* input = "\"ABC\"";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check_strings_equal("ABC", element.as_string);
	mu_check(element.type == ELEMENT_STRING);
	mu_check(pos == input + 5);
	mu_check(*pos == '\0');

	free_element(element);

	mu_end();
}

static int _test_parse_element_stringInvalid() {
	mu_start();

	Element element;
	char const* input = "ABC";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(!is_success);
	mu_check(pos == input);
	mu_check(*pos == 'A');

	input = "ABC\"";
	pos = input;
	is_success = parse_element(&element, &pos);
	mu_check(!is_success);
	mu_check(pos == input);
	mu_check(*pos == 'A');

	mu_end();
}

static int _test_print_element_int() {
	mu_start();

	Element element;
	char const* input = "123";
	bool is_success = parse_element(&element, &input);
	mu_check(is_success);

	printf("Testing parse_element(&element, \"123\")\n");
	printf(" - Expected: 123\n");
	printf(" - Actual:  ");
	print_element(element);
	fputc('\n', stdout);
	//free_element(element);

	mu_end();
}

static int _test_print_element_string() {
	mu_start();

	Element element;
	char const* input = "\"ABC\"";
	bool is_success = parse_element(&element, &input);
	mu_check(is_success);	
	printf("Testing parse_element(&element, \"\\\"ABC\\\"\")\n");
	printf(" - Expected: \"ABC\"\n");
	printf(" - Actual:  ");
	print_element(element);
	
	free_element(element);

	mu_end();
}

//PARSE LIST
static int _test_parse_empty_list_valid() {
	mu_start();

	Element element;
	char const* input = "[]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.type == ELEMENT_LIST);
	mu_check(pos == input + 2);
	mu_check(*pos == '\0');
	mu_check(element.as_list == NULL);

	mu_end();
}

static int _test_parse_list_IntBasic_valid() {
	mu_start();

	Element element;
	char const* input = "[1,2]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.type == ELEMENT_LIST);
	mu_check(pos == input + 5);
	mu_check(*pos == '\0');
	mu_check(element.as_list != NULL);
	mu_check(element.as_list -> element.as_int == 1);
	mu_check(element.as_list -> next -> element.as_int == 2);
	mu_check(element.as_list -> next -> element.type == ELEMENT_INT);
	//mu_check(element.as_list -> next -> next -> element.as_list == NULL);
	print_element(element);
	free_element(element);

	fputc('\n',stdout);

	mu_end();
}

static int _test_parse_list_IntHarder_valid() {
	mu_start();

	Element element;
	char const* input = "[123,456,789]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.type == ELEMENT_LIST);
	mu_check(pos == input + 13);
	mu_check(*pos == '\0');
	mu_check(element.as_list != NULL);
	mu_check(element.as_list -> element.as_int == 123);
	mu_check(element.as_list -> next -> element.as_int == 456);
	mu_check(element.as_list -> next -> next ->  element.as_int == 789);
	fputc('\n', stdout);
	print_element(element);

	free_element(element);

	mu_end();
}

static int _test_parse_list_StringBasic_valid() {
	mu_start();

	Element element;
	char const* input = "[\"ABC\"]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.type == ELEMENT_LIST);
	mu_check(pos == input + 7);
	mu_check(*pos == '\0');
	mu_check(element.as_list != NULL);
	mu_check_strings_equal("ABC", element.as_list -> element.as_string);
	free_element(element);

	mu_end();
}

static int _test_parse_list_StringBasic2_valid() {
	mu_start();

	Element element;
	char const* input = "[\"ABC\",\"DEF\"]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.type == ELEMENT_LIST);
	mu_check(pos == input + 13);
	mu_check(*pos == '\0');
	mu_check(element.as_list != NULL);
	//mu_check_strings_equal("ABC", element.as_list -> element.as_string);
	mu_check_strings_equal("ABC", element.as_list -> element.as_string);
	//mu_check(element.as_list -> next -> element.as_int == 456);
	fputc('\n', stdout);
	print_element(element);

	free_element(element);

	mu_end();
}

static int _test_parse_list_StringHarder_valid() {
	mu_start();

	Element element;
	char const* input = "[\"ABC\", 456]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.type == ELEMENT_LIST);
	mu_check(pos == input + 12);
	mu_check(*pos == '\0');
	mu_check(element.as_list != NULL);
	mu_check_strings_equal("ABC", element.as_list -> element.as_string);
	//mu_check_strings_equal("DEF", element.as_list -> next -> element.as_string);
	mu_check(element.as_list -> next -> element.as_int == 456);
	fputc('\n', stdout);
	print_element(element);

	free_element(element);

	mu_end();
}

static int _test_parse_list_StringIntSupremeTest_valid() {
	mu_start();

	fputc('\n', stdout);
	Element element;
	char const* input = "[\"ABC\", 456, \"123456789\", 123456789, \"Miguel\", \"H3ll0 W0rld\", -69420, [[123, 789]]]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.type == ELEMENT_LIST);
	mu_check(pos == input + 83);
	mu_check(*pos == '\0');
	mu_check(element.as_list != NULL);
	//mu_check_strings_equal("ABC", element.as_list -> element.as_string);
	mu_check(element.as_list -> next -> element.as_int == 456);
	mu_check_strings_equal("123456789", element.as_list -> next -> next -> element.as_string);
	mu_check(element.as_list -> next -> next -> next ->  element.as_int == 123456789);
	mu_check_strings_equal("Miguel", element.as_list -> next -> next -> next -> next ->element.as_string);
	mu_check_strings_equal("H3ll0 W0rld", element.as_list -> next -> next -> next -> next -> next -> element.as_string);
	mu_check(element.as_list -> next -> next -> next -> next -> next -> next -> element.as_int == -69420);

	fputc('\n', stdout);
	print_element(element);
	
	free_element(element);

	mu_end();
}

static int _test_parse_list_nestedList_valid() {
	mu_start();

	Element element;
	char const* input = "[1,[2,3,\"ABC\",5],6]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.type == ELEMENT_LIST);
	mu_check(pos == input + 19);
	mu_check(*pos == '\0');
	mu_check(element.as_list != NULL);
	mu_check(element.as_list -> element.as_int == 1);
	mu_check(element.as_list -> next -> element.type == ELEMENT_LIST);
    mu_check(element.as_list -> next -> next -> element.as_int == 6);
	fputc('\n', stdout);
	print_element(element);

	free_element(element);

	mu_end();
}

static int _test_parse_list_nestedList_valid2() {
	mu_start();

	Element element;
	char const* input = "[[]]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.type == ELEMENT_LIST);
	mu_check(pos == input + 4);
	mu_check(*pos == '\0');
	fputc('\n', stdout);
	print_element(element);

	free_element(element);

	mu_end();
}

static int _test_parse_list_nestedList_valid3() {
	mu_start();

	Element element;
	char const* input = "[[9]]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.type == ELEMENT_LIST);
	mu_check(pos == input + 5);
	mu_check(*pos == '\0');
	fputc('\n', stdout);
	print_element(element);

	free_element(element);

	mu_end();
}

static int _test_parse_list_nestedList_valid4() {
	mu_start();

	Element element;
	char const* input = "[[123],[456]]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.type == ELEMENT_LIST);
	mu_check(pos == input + 13);
	mu_check(*pos == '\0');
	free_element(element);

	mu_end();
}

static int _test_parse_list_nestedList_valid5() {
	mu_start();

	Element element;
	char const* input = "[[\"hello\", \"world\"],[456, 7]]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);	
	mu_check(pos == input + 29);
	mu_check(*pos == '\0');
	mu_check(element.type == ELEMENT_LIST);
	mu_check(element.as_list -> next -> element.type == ELEMENT_LIST);
	free_element(element);

	mu_end();
}

static int _test_parse_list_nestedList_valid6() {
	mu_start();

	Element element;
	char const* input = "[123456789]mgiuel";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(is_success);
	mu_check(element.type == ELEMENT_LIST);
	mu_check(pos == input + 11);
	mu_check(*pos == 'm');
	mu_check(element.as_list -> element.as_int == 123456789);
	free_element(element);

	mu_end();
}

static int _test_parse_list_invalidHard1() { //THIS IS THE ONE THAT'S GIVING ME A MEMORY LEAK
	mu_start();

	Element element;
	char const* input = "[\"ABC\", --4]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(!is_success);
	mu_check(pos == input + 9); //The error comes from adding too much to *a_pos
	mu_check(*pos == '-');
	mu_end();
}

static int _test_parse_list_invalidHard2() {
	mu_start();

	Element element;
	char const* input = "[ABC, -4]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(!is_success);
	mu_check(pos == input + 1); //The error comes from adding too much to *a_pos
	mu_check(*pos == 'A');
	mu_end();
}

static int _test_parse_list_invalid1() {
	mu_start();

	Element element;
	char const* input = "[";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(!is_success);
	mu_check(pos == input + 1);
	mu_check(*pos == '\0');
	mu_end();
}

static int _test_parse_list_invalid2() {
	mu_start();

	Element element;
	char const* input = "][";//In here it won't even call parse list since we don't have to
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(!is_success);
	mu_check(pos == input);
	mu_check(*pos == ']');
	mu_end();
}

static int _test_parse_list_invalid3() {
	mu_start();

	Element element;
	char const* input = "A[]";//In here it won't even call parse list since we don't have to
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(!is_success);
	mu_check(pos == input);
	mu_check(*pos == 'A');
	mu_end();
}

static int _test_parse_list_invalid4() {
	mu_start();

	Element element;
	char const* input = "[[";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(!is_success);
	mu_check(pos == input + 2);
	mu_check(*pos == '\0');

	mu_end();
}

static int _test_parse_list_invalid5() {
	mu_start();

	Element element;
	char const* input = "[1,2,,3]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(!is_success);
	mu_check(pos == input + 5);
	mu_check(*pos == ',');
	mu_end();
}

static int _test_parse_list_invalid6() {
	mu_start();

	Element element;
	char const* input = ",2]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(!is_success);
	mu_check(pos == input);
	mu_check(*pos == ',');
	mu_end();
}

static int _test_parse_list_invalid7() {
	mu_start();

	Element element;
	char const* input = "[1 2, 3]";
	char const* pos = input;
	bool is_success = parse_element(&element, &pos);
	mu_check(!is_success);
	mu_check(pos == input + 3);
	mu_check(*pos == '2');
	mu_end();
}

int main(int argc, char* argv[]) {
	//int stringLen = strlen("\"ABC\"");
	//printf("%d", stringLen);
	
	//parse int 
	
	mu_run(_test_parse_int_valid);
	mu_run(_test_parse_integer);
	mu_run(_test_parse_int_invalid);
	mu_run(_test_parse_int_negative);
	mu_run(_test_parse_int_withBreak);
	mu_run(_test_parse_int_negativeWithBreak);
	mu_run(_test_parse_int_negativeInvalid);

	//////////////////
	//PARSE STRINGS//
	
	mu_run(_test_parse_string_valid_empty);
	mu_run(_test_parse_string_valid_one_char);
	mu_run(_test_parse_string_invalid);
	mu_run(_test_parse_string_invalid2);
	mu_run(_test_parse_string_invalid3);
	mu_run(_test_parse_string_invalid4);
	mu_run(_test_parse_string_valid_multiple_chars);
	mu_run(_test_parse_string_valid_complicated);

	//PARSE ELEMENT
	//
	mu_run(_test_parse_element_int_plain);
	mu_run(_test_parse_element_with_leading_whitespace);
	mu_run(_test_parse_element_int_oddballs);
	mu_run(_test_parse_element_invalid);
	mu_run(_test_parse_element_string);
	mu_run(_test_parse_element_empty_invalid);

	//PRINT ELEMENT
	mu_run(_test_print_element_int);
	mu_run(_test_print_element_string);
	mu_run(_test_parse_element_stringInvalid);

	//PARSE LIST
	mu_run(_test_parse_empty_list_valid);
	mu_run(_test_parse_list_IntBasic_valid);
	mu_run(_test_parse_list_IntHarder_valid);
	mu_run(_test_parse_list_StringBasic_valid);
	mu_run(_test_parse_list_StringBasic2_valid);
	mu_run(_test_parse_list_StringHarder_valid);
	mu_run(_test_parse_list_nestedList_valid);
	mu_run(_test_parse_list_nestedList_valid2);
	mu_run(_test_parse_list_nestedList_valid3);
	mu_run(_test_parse_list_nestedList_valid4);
	mu_run(_test_parse_list_nestedList_valid5);
	mu_run(_test_parse_list_nestedList_valid6);
	mu_run(_test_parse_list_StringIntSupremeTest_valid);

	mu_run(_test_parse_list_invalidHard1);
	mu_run(_test_parse_list_invalidHard2);
	mu_run(_test_parse_list_invalid1);
	mu_run(_test_parse_list_invalid2);
	mu_run(_test_parse_list_invalid3);
	mu_run(_test_parse_list_invalid4);
	mu_run(_test_parse_list_invalid5);
	mu_run(_test_parse_list_invalid6);
	mu_run(_test_parse_list_invalid7);
	
	
	return EXIT_SUCCESS;
}

/* vim: set tabstop=4 shiftwidth=4 fileencoding=utf-8 noexpandtab: */
