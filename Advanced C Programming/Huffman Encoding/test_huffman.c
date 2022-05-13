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
#include "bit_writer.h"


static void _destroy_string(void* string) {
	//free(string);
}


static void _destroy_int(void* integer) {
	
}



static int _cmp_strings_by_length(const void* a_lhs, const void* a_rhs) {
	size_t len_lhs = strlen(a_lhs); // No typecast needed!  Never use typedcast unless:
	size_t len_rhs = strlen(a_rhs); // (a) necessary, (b) safe, and (c) well-understood.
	return len_lhs - len_rhs; // shortest string comes forst
}


int _compare_fn_for_qsort(const void* o1, const void* o2)
{
	return((*(int*)o1) - (*(int*)o2));
}

/*
static int _string_cmp(const void* p1, const void* p2) {
	   return strcmp((const char*)p1, (const char*)p2);
}
*/

//TESTS


static int _testDemoStringLength()
{
	mu_start();

	Node* head = NULL;  // size 0
	pq_enqueue(&head, "MiguelCastilho", _cmp_strings_by_length);  // size 1
	pq_enqueue(&head, "was", _cmp_strings_by_length);  // size 2
	pq_enqueue(&head, "an", _cmp_strings_by_length);  // size 3
	pq_enqueue(&head, "amazingMAN", _cmp_strings_by_length);  // size 4

	mu_check(head -> a_value = "an");
	mu_check(head -> next -> a_value = "was");
	mu_check(head -> next -> next -> a_value = "amazingMAN");
	mu_check(head -> next -> next -> next -> a_value = "MiguelCastilho");

	destroy_list(&head, _destroy_string);

	mu_end();

}


static int _testDemoInteger()
{
	mu_start();
	Node* head = NULL;

	int m = 9;
	pq_enqueue(&head, &m,_compare_fn_for_qsort);
	mu_check(head != NULL);
	mu_check(head -> a_value == &m);

	
	int n = 15;
	pq_enqueue(&head, &n,_compare_fn_for_qsort);
	mu_check(head -> a_value == &m);
	mu_check(head -> next -> a_value == &n);

	int o = 12;
	pq_enqueue(&head, &o,_compare_fn_for_qsort);
	mu_check(head -> a_value == &m);
	mu_check(head -> next -> a_value == &o);
	mu_check(head -> next -> next ->a_value == &n);

	int p = 10;
	//pq_enqueue(&head, &o,_compare_fn_for_qsort);
	stack_push(&head, &p);
	mu_check(head -> a_value == &p);
	mu_check(head -> next -> a_value == &m);
	mu_check(head -> next -> next ->a_value == &o);

	Node* removedNode;
	removedNode = stack_pop(&head);
	destroy_list(&removedNode, _destroy_int);
	mu_check(head -> a_value == &m);
	mu_check(head -> next -> a_value == &o);
	mu_check(head -> next -> next ->a_value == &n);


	destroy_list(&head, _destroy_int); 

	mu_end();

}

static void _destroyTree(void* tree)
{
	free((TreeNode*)tree);
}

static int _test1TXT()
{
	mu_start();

	Frequencies freqs = {0};
	const char* filename = "./test1.txt";
	const char* a_error;
	bool validFile;

	validFile = calc_frequencies(freqs, filename, &a_error);
 
	mu_check(freqs['a'] == 5);
	mu_check(freqs['b'] == 1);
	mu_check(freqs['P'] == 2);
	mu_check(freqs['7'] == 1);
	mu_check(validFile ==true);

	mu_end();
}


static int _testFail()
{
	mu_start();

	Frequencies freqs = {0};
	const char* filename = "./test4.txt";
	const char* a_error = NULL;
	bool validFile;

	validFile = calc_frequencies(freqs, filename, &a_error);
 
	mu_check(!(validFile));

	mu_end();

}


static int _testHuffman()
{
	mu_start();

	Frequencies freqs = {0};
	const char* filename = "./test2.txt";
	const char* error;
	bool validFile;

	validFile = calc_frequencies(freqs, filename, &error);
	mu_check(validFile);

	mu_check(freqs['m'] == 3);
	mu_check(freqs['i'] == 2);
	mu_check(freqs['g'] == 2);
	mu_check(freqs['u'] == 1);
	mu_check(freqs['e'] == 1);
	mu_check(freqs['l'] == 1);


	Node* newListhead = make_huffman_pq(freqs);

	mu_check(newListhead != NULL);
	mu_check( ((TreeNode*)(newListhead -> a_value)) -> character == 10); 
	mu_check( ((TreeNode*)(newListhead -> a_value)) -> frequency == 1);

	mu_check( ((TreeNode*)(newListhead ->next->a_value)) -> character == 'e');
	mu_check( ((TreeNode*)(newListhead ->next->a_value)) -> frequency == 1);	

	mu_check( ((TreeNode*)(newListhead ->next->next->a_value)) -> character == 'l');
	mu_check( ((TreeNode*)(newListhead ->next->next->a_value)) -> frequency == 1);	

	mu_check( ((TreeNode*)(newListhead ->next->next->next->a_value)) -> character == 'u');
	mu_check( ((TreeNode*)(newListhead ->next->next->next->a_value)) -> frequency == 1);	

	mu_check( ((TreeNode*)(newListhead ->next->next->next->next->a_value)) -> character == 'g');
	mu_check( ((TreeNode*)(newListhead ->next->next->next->next->a_value)) -> frequency == 2);	

	mu_check( ((TreeNode*)(newListhead ->next->next->next->next->next->a_value)) -> character == 'i');
	mu_check( ((TreeNode*)(newListhead ->next->next->next->next->next->a_value)) -> frequency == 2);

	mu_check( ((TreeNode*)(newListhead ->next->next->next->next->next->next->a_value)) -> character == 'm');
	mu_check( ((TreeNode*)(newListhead ->next->next->next->next->next->next->a_value)) -> frequency == 3);

	destroy_list(&newListhead, _destroyTree);

	mu_end();

}


static int _testHuffmanTreeSimple()
{
	mu_start();

	Frequencies freqs = {0};
	const char* filename = "./testSimple.txt";
	const char* a_error;
	bool validFile = calc_frequencies(freqs, filename, &a_error);
	
	mu_check(validFile);
	mu_check(freqs['a'] == 1);
	mu_check(freqs['b'] == 2);

	Node* newListHead = make_huffman_pq(freqs);

	TreeNode* huffmanTree = make_huffman_tree(newListHead);

	mu_check(huffmanTree -> character == '\0');

	mu_check(huffmanTree -> frequency == 4);


	mu_check(huffmanTree ->left-> character == 'b');

	mu_check(huffmanTree ->left-> frequency == 2);


	mu_check(huffmanTree ->right->character == '\0');
	
	mu_check(huffmanTree ->right->frequency == 2);

	
	mu_check(huffmanTree ->right->left->character == '\n');

	mu_check(huffmanTree ->right->right->character == 'a');

	destroy_huffman_tree(&huffmanTree);

	mu_end();

}


static int _testHuffmanTree1()
{
	mu_start();

	Frequencies freqs = {0};
	const char* filename = "./test1.txt";
	const char* a_error;
	bool validFile;

	validFile = calc_frequencies(freqs, filename, &a_error);
 
	mu_check(freqs['a'] == 5);
	mu_check(freqs['b'] == 1);
	mu_check(freqs['P'] == 2);
	mu_check(freqs['7'] == 1);
	mu_check(validFile ==true);

	Node* newListHead = make_huffman_pq(freqs);

	TreeNode* huffmanTree = make_huffman_tree(newListHead);

	mu_check(huffmanTree -> character == '\0');

	mu_check(huffmanTree -> frequency == 11);

	destroy_huffman_tree(&huffmanTree);

	mu_end();
}

static int _testHuffmanTree2()
{
	mu_start();

	Frequencies freqs = {0};
	const char* filename = "./test2.txt";
	const char* error;
	bool validFile;

	validFile = calc_frequencies(freqs, filename, &error);
	mu_check(validFile);

	mu_check(freqs['m'] == 3);
	mu_check(freqs['i'] == 2);
	mu_check(freqs['g'] == 2);
	mu_check(freqs['u'] == 1);
	mu_check(freqs['e'] == 1);
	mu_check(freqs['l'] == 1);


	Node* newListHead = make_huffman_pq(freqs);

	TreeNode* huffmanTree = make_huffman_tree(newListHead);

	mu_check(huffmanTree -> character == '\0');

	mu_check(huffmanTree -> frequency == 11);

	destroy_huffman_tree(&huffmanTree);

	mu_end();

}

static int _testHuffmanTreeEmpty()
{
	mu_start();

	Frequencies freqs = {0};
	const char* filename = "./testEmpty.txt";
	const char* error;
	//bool validFile;

	calc_frequencies(freqs, filename, &error);
	//mu_check(validFile);

	Node* newListHead = make_huffman_pq(freqs);

	TreeNode* huffmanTree = make_huffman_tree(newListHead);

	mu_check(huffmanTree == NULL);

	//destroy_huffman_tree(&huffmanTree);

	mu_end();

}

static int _testFirstIf() {
	mu_start();
	//────────────────────
	BitWriter  writer = open_bit_writer("newFile.bits");
	write_bits(&writer,0x05,3);

	mu_check((&writer) -> current_byte != 0x05);	
	mu_check((&writer) -> current_byte == 0xa0);
	mu_check((&writer) -> num_bits_left == 5);

	write_bits(&writer,0x10,5);

	mu_check((&writer) -> current_byte == 0x00);
	mu_check((&writer) -> num_bits_left == 8);

	close_bit_writer(&writer);

	mu_check((&writer) -> num_bits_left == 8);
	mu_check((&writer) -> current_byte == 0);
	
	//────────────────────
	mu_end();
}

static int _testElse() {
	mu_start();
	//────────────────────
	
	BitWriter  writer = open_bit_writer("newFile2.bits");
	write_bits(&writer,0x05,3);

	mu_check((&writer) -> current_byte != 0x05);	
	mu_check((&writer) -> current_byte == 0xa0);
	mu_check((&writer) -> num_bits_left == 5);

	write_bits(&writer, 0x3f,6);
	mu_check((&writer) -> num_bits_left == 7);
	mu_check((&writer) -> current_byte != 0);
	mu_check((&writer) -> current_byte == 0x80);

	close_bit_writer(&writer);
	mu_check((&writer) -> num_bits_left == 8);
	mu_check((&writer) -> current_byte == 0);

	
	//────────────────────
	mu_end();
}


static int _testEncodingTreeToAFile1() {
	mu_start();
	//────────────────────
	Frequencies freqs = {0};
	const char* filename = "./testSimple2.txt";
	const char* error;
	bool validFile;

	validFile = calc_frequencies(freqs, filename, &error);
	mu_check(validFile);

	Node* newListHead = make_huffman_pq(freqs);

	TreeNode* huffmanTree = make_huffman_tree(newListHead);
	
	BitWriter writer = open_bit_writer("testWriteCodingTable.bits");

	write_coding_table(huffmanTree, &writer);

	
	mu_check((&writer) -> current_byte == 0x20);

	mu_check((&writer) -> num_bits_left == 3);

	close_bit_writer(&writer);

	mu_check((&writer) -> num_bits_left == 8);
	mu_check((&writer) -> current_byte == 0);

	destroy_huffman_tree(&huffmanTree);
	
	//────────────────────
	mu_end();
}

static int _testEncodingTreeToAFile2() 
{
	mu_start();
	//────────────────────
	Frequencies freqs = {0};
	const char* filename = "./testSimple3.txt";
	const char* error;
	bool validFile;

	validFile = calc_frequencies(freqs, filename, &error);
	mu_check(validFile);

	Node* newListHead = make_huffman_pq(freqs);

	TreeNode* huffmanTree = make_huffman_tree(newListHead);
	
	BitWriter writer = open_bit_writer("testWriteCodingTable2.bits");

	write_coding_table(huffmanTree, &writer);

	
	mu_check((&writer) -> current_byte == 0x10);

	mu_check((&writer) -> num_bits_left == 1);
		
	close_bit_writer(&writer);

	mu_check((&writer) -> num_bits_left == 8);
	mu_check((&writer) -> current_byte == 0);

	destroy_huffman_tree(&huffmanTree);

	
	//────────────────────
	mu_end();
}

static int _testEncoding3() 
{
	mu_start();
	//────────────────────
	Frequencies freqs = {0};
	const char* filename = "./testSimple4.txt";
	const char* error;
	bool validFile;

	validFile = calc_frequencies(freqs, filename, &error);
	mu_check(validFile);

	Node* newListHead = make_huffman_pq(freqs);

	TreeNode* huffmanTree = make_huffman_tree(newListHead);
	
	BitWriter writer = open_bit_writer("testWriteCodingTable3.bits");

	write_coding_table(huffmanTree, &writer);
	
	close_bit_writer(&writer);

	mu_check((&writer) -> num_bits_left == 8);
	mu_check((&writer) -> current_byte == 0);

	destroy_huffman_tree(&huffmanTree);

	
	//────────────────────
	mu_end();
}


static int _testCompressed1() 
{
	mu_start();
	//────────────────────
	Frequencies freqs = {0};
	const char* filename = "./testSimple4.txt";
	const char* error;
	uint8_t* uncompressedBits = (unsigned char*) "huffman fluffs many mums";

	calc_frequencies(freqs, filename, &error);
	freqs['\0'] = 0;
	freqs['\n'] = 0;

	Node* newListHead = make_huffman_pq(freqs);

	TreeNode* huffmanTree = make_huffman_tree(newListHead);
	
	BitWriter writer = open_bit_writer("testWriteCodingTable4.bits");

	write_compressed(huffmanTree, &writer,uncompressedBits);
	
	close_bit_writer(&writer);

	destroy_huffman_tree(&huffmanTree);

	//────────────────────
	mu_end();
}

static int _testCompressed2() 
{
	mu_start();
	//────────────────────
	Frequencies freqs = {0};
	const char* filename = "./testSimple7.txt";
	const char* error;
	uint8_t* uncompressedBits = (unsigned char*) "m";

	calc_frequencies(freqs, filename, &error);
	freqs['\0'] = 0;
	freqs['\n'] = 0;

	Node* newListHead = make_huffman_pq(freqs);

	TreeNode* huffmanTree = make_huffman_tree(newListHead);
	
	BitWriter writer = open_bit_writer("testWriteCodingTable5.bits");

	write_compressed(huffmanTree, &writer,uncompressedBits);
	
	close_bit_writer(&writer);

	destroy_huffman_tree(&huffmanTree);

	//────────────────────
	mu_end();
}

int main(int argc, char* argv[]) 
{

	//mu_run(_testDemoInteger);
	
	mu_run(_test1TXT);
	mu_run(_testFail);
	mu_run(_testHuffman);
	mu_run(_testDemoStringLength);
	mu_run(_testDemoInteger);
	mu_run(_testHuffmanTreeSimple);
	mu_run(_testHuffmanTree1);
	mu_run(_testHuffmanTree2);
	mu_run(_testHuffmanTreeEmpty);
	mu_run(_testFirstIf);
	mu_run(_testElse);
	mu_run(_testEncodingTreeToAFile1);
	mu_run(_testEncodingTreeToAFile2);
	mu_run(_testEncoding3); 
	mu_run(_testCompressed1);
	mu_run(_testCompressed2);

	return EXIT_SUCCESS;
}
/* vim: set tabstop=4 shiftwidth=4 fileencoding=utf-8 noexpandtab: */
