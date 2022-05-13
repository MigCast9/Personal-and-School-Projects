#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include <errno.h>
#include <string.h>
#include "miniunit.h"
#include "clog.h"
#include "frequencies.h"
#include "priority_queue.h"
#include "huffman.h"

//const int _cmp_fn(void* var1, void* var2);
//static int _cmp_fn(const void* var1, const void* var2)
typedef struct _BitCode
{
	uint8_t bits;
	int numBits;

} BitCode;

void _lookUpTableCreator(TreeNode* root, BitCode* charToCode, int counter, uint8_t bit);

static int _cmp_fn(const void* var1, const void* var2)
{
	int diff = (*(TreeNode*)var1).frequency - (*(TreeNode*)var2).frequency;
	if (diff)
	{
		return diff;
	}
	if ((*(TreeNode*)var1).character == '\0' || (*(TreeNode*) var2).character == '\0')
	{
		return (*(TreeNode*)var2).character - (*(TreeNode*)var1).character;
	}
	return(*(TreeNode*)var1).character - (*(TreeNode*)var2).character;
}

Node* make_huffman_pq(Frequencies freqs)
{	
	Node* headNewList = NULL;
	
	for (unsigned int ch = 0; ch < 256; ch++)
	{
		if (freqs[ch] != 0)
		{
			TreeNode* treeAddress = malloc(sizeof(*treeAddress)); //Allocating space for tree
			*treeAddress = (TreeNode) {.character = ch, .frequency = freqs[ch], .right = NULL, .left = NULL}; //initializing tree node
			pq_enqueue(&headNewList,treeAddress , _cmp_fn);
		}
	}

	return(headNewList);
}

TreeNode* make_huffman_tree(Node* head)
{
	if (head == NULL)//if the node is empty
	{
		return NULL;
	}

	//Create space for the cluster node
		
	while (head -> next != NULL)
	{
		TreeNode* clusterNode = malloc(sizeof(*clusterNode));
			
		//Grab the first node of the sorted linked list and store its frequency
		size_t frequencyNode1 = ((TreeNode*)(head->a_value))->frequency;
		Node* removedNode1 = pq_dequeue(&head);

		//Grab the second node of the linked list and store its frequency
		size_t frequencyNode2 = ((TreeNode*)(head->a_value))->frequency;
		Node* removedNode2 = pq_dequeue(&head);

		//Create the cluster node, initializing its character to NULL, the frequency to the sum of the frequencies and the left and right
		//branches to whatever the first two nodes of the list were pointing to
		*clusterNode = (TreeNode) {.character = '\0', .frequency = (frequencyNode1 + frequencyNode2), .right = removedNode2->a_value, .left = removedNode1->a_value};

		//Free the two removed nodes as they are no longer being used

		free(removedNode1);
		free(removedNode2);

		//Use pq_enqueue to put the new cluster in the linked list
		pq_enqueue(&head,clusterNode,_cmp_fn);
							
	}

	TreeNode* clusterFinalSupreme = head -> a_value; //create a copy of your tree so that you can free the node from the linked list
	
	//Free the head of the list once there is only one node
	free(head);
	
	return(clusterFinalSupreme);	
}

void destroy_huffman_tree(TreeNode** a_root)
{
	if (*a_root != NULL)
	{
		destroy_huffman_tree(&((*a_root) ->left));
		destroy_huffman_tree(&((*a_root) ->right));
		free(*a_root);
	}
	*a_root = NULL;
}

//The writer object created in the test file is what goes inside
//Output of make_huffman_tree is what goes inside, also created in the test file
void write_coding_table(TreeNode* root, BitWriter* a_writer)
{
	if (root != NULL)
	{
		write_coding_table(root ->left, a_writer);
		write_coding_table(root ->right, a_writer);
		
		if (root -> character != '\0')
		{
			write_bits(a_writer, 0x01, 1);
			write_bits(a_writer, root->character, 8);
		}

		else 
		{
			write_bits(a_writer, 0x00, 1);
		}
		
	}
	//root = NULL;
	
}

/*
void my_print_bits(BitCode element) {
	uint8_t mask = 0x01;
	for (int i = element.numBits - 1; i; i -= 1) {
		mask <<= 1;
	}
	for (uint8_t bits = element.bits; mask; mask >>= 1) {
		fputc(!!(bits & mask) + '0', stdout);
	}
}*/

void write_compressed(TreeNode* root, BitWriter* a_writer, uint8_t* uncompressed_bytes)
{
	//Here we initialize the lookup table with empty parameters
	BitCode charCompressedTable[256] = {(BitCode) {.bits = 0, .numBits = 0}};

	//Here we get the lookup table
	_lookUpTableCreator(root, charCompressedTable, 0, 0);

	/*
	for (int i = 0; i < sizeof(charCompressedTable)/sizeof(*charCompressedTable); i += 1) {
		if (charCompressedTable[i].numBits) {
			printf("\n%c: ", i);
			my_print_bits(charCompressedTable[i]);
		}
	}
	printf("\n");*/
	
	//loop to iterate through the string stopping at the null character
	while (*uncompressed_bytes != '\0')
	{
		//Save the *uncompressed_bytes in an index
		int charIndex = *uncompressed_bytes;

		//Save the bit encoding and number of bits from that character to a variable
		uint8_t bitEncoding = (charCompressedTable[charIndex]).bits;
		int numberBits = (charCompressedTable[charIndex]).numBits;
		
		//call write bits to write the encoded character in a file
		write_bits(a_writer, bitEncoding, numberBits);

		//updates the character being looked at
		uncompressed_bytes += 1;
	}
}

//This function will output the lookupTable
void _lookUpTableCreator(TreeNode* root, BitCode* charToCode, int counter, uint8_t bit)
{
	if (root != NULL)
	{
	
		//Here we set the bits and numBits types of our struct to the bit variable and counter respectively	
		_lookUpTableCreator(root->left, charToCode, counter+1, bit << 1);
		_lookUpTableCreator(root->right, charToCode, counter+1, (bit << 1) | 0x01);
		if (root -> character!= '\0')
		{
			charToCode[root->character] = (BitCode) {.bits = bit, .numBits = counter};
		}
	}

	/*
	
		if (root -> left != NULL)
		{
			_lookUpTableCreator(root -> left, charToCode, counter + 1, bit << 1);
		}

		if (root -> right != NULL)
		{
			_lookUpTableCreator(root -> right, charToCode, counter + 1, (bit << 1) | 0x01);
			
		}
		
		if (root -> character != '\0')
		{
			(charToCode[root -> character]).bits = bit;
			(charToCode[root -> character]).numBits = counter;
		}
				
	}*/

}
