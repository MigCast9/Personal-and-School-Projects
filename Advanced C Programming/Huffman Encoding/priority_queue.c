#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include "huffman.h"


Node* pq_enqueue(Node** a_head, void* a_value, int (*cmp_fn)(const void*, const void*)) 
{
	Node* newNode = malloc(sizeof(*newNode));
	*newNode = (Node) { .a_value = a_value, .next = *a_head};

	if (*a_head == NULL ||cmp_fn(((*a_head) -> a_value), a_value) > 0) // || cmp_fn == NULL)
	{
		*a_head = newNode;//update a_head to point to the newNode which points to what used to be the first item i nthe list
	}

	else
	{
		Node* temp = *a_head;
		while (temp->next != NULL && cmp_fn(temp->next->a_value, a_value) <= 0) 
		{
			temp = temp->next;
		}
		newNode->next = temp->next;
		temp->next = newNode;
	}	
	
	
	return newNode;  // STUB -- remove this line when filling in the body of pq_enqueue(…).
}


Node* pq_dequeue(Node** a_head) 
{
	Node* removedNode = *a_head;
	if (removedNode != NULL)
	{
		*a_head = (*a_head) -> next; //set the address of the head to be the address of the next element in order to isolate the old head
		removedNode -> next = NULL; //set the address that the removed node points to to be NULL
	
	}
	
	return removedNode;  // STUB -- remove this line when filling in the body of pq_dequeue(…).
}


Node* stack_push(Node** a_head, void* a_value) 
{
	Node* newNode = malloc(sizeof(*newNode));
	*newNode = (Node) { .a_value = a_value, .next = *a_head};
	*a_head = newNode;

	return newNode;  // STUB -- remove this line when filling in the body of stack_push(…).
}


Node* stack_pop(Node** a_head) 
{
	return pq_dequeue(a_head);  // STUB -- remove this line when filling in the body of stack_pop(…).
}


void destroy_list(Node** a_head, void (*destroy_value_fn)(void*)) 
{
	//for (Node* newHead; *a_head != NULL; *a_head = newHead) 
	while(*a_head != NULL)
	{

		Node* newHead = (*a_head) -> next;
		destroy_value_fn((*a_head) -> a_value);
		free(*a_head);
		*a_head = newHead;
	}
	//free(*a_head);
}


#define HUFFMAN_C_V1
