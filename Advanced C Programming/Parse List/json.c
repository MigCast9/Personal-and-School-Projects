#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include "json.h"
#include "clog.h"
#include <string.h>
#include <ctype.h>
#include <limits.h>

void _append(Element value, Node** aHead, Node** aTail);
void _destroy_list(Node* head);

bool parse_int(int* a_value, const char** a_pos)
{
	bool isInteger = false;
	int loopCounter = 0;
	int negativeIndicator = 0;

	//Here if the string starts with a hyphen we add one to the position to look at the next character
	if (**a_pos == '-')
	{
		*a_pos += 1;
		negativeIndicator = 1;
	}

	//here we set the necessary values to *a_value, in which it will only get in if there is a valid string
	while (**a_pos <= '9' && **a_pos >= '0')
	{
		//fputc('M', stdout);

		//In this first IF, a_value becomes whatever the first char of the input string is
		if (loopCounter == 0)
		{
			*a_value = **a_pos - '0';
		}
		
		//After setting a_value to a value, we multiply it by ten and sum the next value of a_pos
		else
		{
			*a_value *= 10;
			*a_value += **a_pos - '0';
		}

		loopCounter += 1;
		*a_pos += 1;
	}

	if (loopCounter > 0)
	{
		isInteger = true;

		if (negativeIndicator == 1)
		{
			*a_value *= -1;
		}

	}
	//printf("%d", *a_value);
	//fputc('\n', stdout);

	return(isInteger);
}

bool parse_string(char** a_s, char const** a_pos)
{
	bool isString = false; //value to be returned

	int stringLength = strlen(*a_pos);
	int nullCharIndex = 0;

	for (int idxInString = 0; (*a_pos)[idxInString] != '\0'; idxInString++)
	{
		//stringLength++;

		if (((*a_pos)[idxInString]) == '\n')
		{
			nullCharIndex = idxInString;
		}

		else if (((*a_pos)[idxInString] == '\"') && (idxInString > 0))
		{
			stringLength = idxInString + 1;
			break;
		}

	}
		
	int newStringIndex = 0; 
	int aPosIndex = 1;

	if (((*a_pos)[0] == '\"' && (*a_pos)[stringLength - 1] == '\"') && (strchr(*a_pos, 10) == NULL))
	{
		if ((stringLength == 1) && (*a_pos)[0] == '\"') //here if the input is a single "\"", it will return false without mallocing
		{
			isString = false;
		}

		else //If the input is different from the above (any true case), it returns true
		{
		

			*a_s = malloc(sizeof(*a_s) * (stringLength - 1)); // creating the empty list with space for null char
		
			(*a_s)[stringLength - 2] = '\0';
		// Here we start at index 1 since at index 0 there is a quotation mark and end one index less than the final index for the same reason
		
			while(aPosIndex < stringLength - 1)
			{

				(*a_s)[newStringIndex] = (*a_pos)[aPosIndex];

				newStringIndex++;
				//aPosIndex++;
				//**a_s = **a_pos;
				//*a_s += 1;
				//*a_pos += 1;

				aPosIndex++;
			}	
		
			isString = true;
			}
	}
	
	if (strchr(*a_pos, 10) == NULL && (*a_pos)[0] == '\"') //Here if there is no new line char and first char is quoation we get in
	{
		*a_pos += stringLength;
	}
	else if ((*a_pos)[0] == '\"') //Here if there is a new line but the first char is still quotation we get in
	{
		*a_pos += nullCharIndex;
	}
	/*else if ((*a_pos)[0] != '\"')//Here if the first char isn't a quotation we get in to say where we got wrong
	{
		*a_pos += 0;
	}*/
	
	return(isString);
}

bool parse_element(Element* a_element, char const** a_pos)
{

	//int numberOfWhiteSpaces = 0;
	while (isspace(**a_pos))
	{
		*a_pos += 1;
		//numberOfWhiteSpaces++;
	}

	bool returnValue = false;

	if (isdigit(**a_pos) || (**a_pos) == '-')
	{
		a_element -> type = ELEMENT_INT;
	 	returnValue = parse_int(&(a_element -> as_int), a_pos);
	}

	else if (**a_pos == '\"')
	{
		a_element -> type = ELEMENT_STRING;
		returnValue = parse_string(&(a_element -> as_string), a_pos);
	}

	else if ((**a_pos) == '[')
	{
		a_element -> type = ELEMENT_LIST;
		returnValue = parse_list(&(a_element -> as_list), a_pos);
	}


	return(returnValue);

}

bool parse_list(Node** a_head, char const** a_pos)
{
	bool isList = false; //value to be returned

	int stringLength = strlen(*a_pos); //Initializing variable to not get an error
	int stringLengthCopy = 0;
	int bracketsOpenRight = 0;
	int bracketsOpenLeft = 0;

	bool validCommas = true; //variable to check if there aren't any sequential commas
	bool validBracketNum = false; //variable to check if the number of brackets is valid

	int stringChecker = 0;

	for (int idxInString = 0; (*a_pos)[idxInString] != '\0'; idxInString++) 
	{

		if (((*a_pos)[idxInString] == '\"') && (((*a_pos)[idxInString - 1] == ',') || ((*a_pos)[idxInString - 1] == ' ')))
		{
			stringChecker = 1;
		}

	
		//BLOCK TO CHECK IF THE VALID PART OF THE STRING HAS ENDED -> NUMBER OF '[' = ']' AND != 0
		//ALSO ENDS WITH THE INDEX OF THE LAST VALID CHAR
		
		if ((*a_pos)[idxInString] == ']') //Finding the number of left facing brackets in the string
		{
			bracketsOpenLeft++;
		}
		else if ((*a_pos)[idxInString] == '[') //Finding the number of right facing brackets in the string
		{
			bracketsOpenRight++;
		}

		if ((bracketsOpenRight == bracketsOpenLeft) && (bracketsOpenRight != 0)) //Check if the number of brackets is coincident
		{
			stringLength = idxInString + 1; //set the string length to be equal to the index of the bracket + 1
			validBracketNum = true;
			break;
		}
		//End of block
		
		//BLOCK TO CHECK IF THERE AREN'T ANY COMMAS IN DIRECT SEQUENCE
		if (idxInString != 0)
		{
			if (((*a_pos)[idxInString] == ',') && ((*a_pos)[idxInString - 1] == ','))
			{
				validCommas = false;
				stringLength = idxInString; //Gets and stores the length of the string until the point that failed
				break;
			}
			
			else if (((*a_pos)[idxInString] == ' ') && (((*a_pos)[idxInString - 1] != ',')) && ((*a_pos)[idxInString - 1] != '[') && stringChecker == 0)
			{
				isList = false;
				stringLength = idxInString + 1;
				break;
			}


		}
		//End of block
	}


	if (((*a_pos)[0] == '[') && ((*a_pos)[stringLength - 1] == ']') && (validCommas == true) && (validBracketNum == true)) 
	{ //Checking if the string is valid before doing the operations
		isList = true;
		stringLengthCopy = stringLength;


		Node* head = NULL;
		Node* tail = NULL;
		Element element;
		*a_pos += 1;
		
		while ((**a_pos) != ']' && ((**a_pos) != ',')) 
		{ //Here we go through the input string, and we skip the commas

			isList = parse_element(&element, a_pos); //Here we get the first element
			if (isList == false)
			{
				_destroy_list(head);
				break;
			}

			/*while (((**a_pos) != ']') && ((**a_pos) != ',')) { //Here we change **a_pos so that it will indicate the next element in the input list
				*a_pos += 1;
			}*/

			if ((**a_pos) == ',') 
			{ //Correction
				*a_pos += 1;

			}
			
			_append(element, &head, &tail);

		}
		*a_head = head;
	}	

	if (isList == true) 
	{
		*a_pos += 1;
	}
	else 
	{
		*a_pos += (stringLength - stringLengthCopy);
	}

	return(isList);
}

void _append(Element value, Node** aHead, Node** aTail) 
{
	//Allocating memory for the new node
	Node* newTail = malloc(sizeof(*newTail));

	*newTail = (Node) { .element = value, .next = NULL};

	//Depending on whether the list was empty we choose our course of action
	if (*aHead == NULL) 
	{ //Set the empty list to NULL
		*aHead = newTail;
	}
	else 
	{ //Connect the old tail to the new tail
		(*aTail) -> next = newTail;
	}

	*aTail = newTail;
}


void _destroy_list(Node* head) 
{
	for (Node* newHead; head != NULL; head = newHead) 
	{
		newHead = head -> next;
		free_element(head -> element);
		free(head);
	}
}

void free_element(Element element) 
{
	if (element.type == ELEMENT_STRING)
	{
		free(element.as_string);
	}
	else if (element.type == ELEMENT_LIST)
	{
		_destroy_list(element.as_list);
	}
}

void print_element(Element element) 
{
	
	if (element.type == ELEMENT_INT)
	{
		printf("%d", element.as_int);
	}
	else if ((element.type == ELEMENT_STRING))
	{
		printf("%s", element.as_string);
	}
	else if ((element.type == ELEMENT_LIST))
	{
		//print_element(element);
		fputc('[',stdout);
		for (Node* newHead; (element.as_list) != NULL; (element.as_list) = newHead) 
		{	
			newHead = element.as_list -> next;
			print_element((element.as_list) -> element);

			if (newHead != NULL) 
			{
				fputc(',',stdout);
			}
		}
		fputc(']',stdout);
	}	
}
