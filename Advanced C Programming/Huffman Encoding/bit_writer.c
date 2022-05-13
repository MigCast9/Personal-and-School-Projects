#include <assert.h>
#include "bit_writer.h"
#include <stdint.h>
#include <stdio.h>

uint8_t _unset_left_bits(uint8_t byte, uint8_t num_bits_to_unset) {
	return (byte & (0xff>>num_bits_to_unset));  // TODO: replace this with a one-line implementation of this function.
}

BitWriter open_bit_writer(const char* path) {
	BitWriter openFile = (BitWriter) {.current_byte = 0, .num_bits_left = 8, .file = fopen(path,"w")};
	return(openFile);
}


void write_bits(BitWriter* a_writer, uint8_t bits, uint8_t num_bits_to_write) {
	assert(num_bits_to_write >= 0 && num_bits_to_write <= 8);
	assert(a_writer->num_bits_left > 0 && a_writer->num_bits_left <=8); 

	if (num_bits_to_write != 0) {
		
		//Get everything we dont need to the left to be zero		
		bits = _unset_left_bits(bits, 8 - num_bits_to_write); 		
	
		if (num_bits_to_write <= a_writer -> num_bits_left) {	
			//Shift to the left the amount necessary to move it leaving enough space to the right (Ex: bits = 11111111 with numBitsWrite = 2 becomes 11000000)
			bits = bits << ((a_writer -> num_bits_left) - num_bits_to_write); 	

			//update the current byte variable to add the new bits variable in the correct spot and the with the correct number of bits
			a_writer -> current_byte = bits | (a_writer -> current_byte);

			//Here we update the number of bits left based on the number of bits to write
			a_writer -> num_bits_left = (a_writer -> num_bits_left) - num_bits_to_write;
		
			//Here we check to see if the number of bits left is zero in order to call flush bit writer to print them and reset the count
			if ((a_writer -> num_bits_left) == 0) {
				flush_bit_writer(a_writer);
			}	
		}

		//Else statemente in case the number of bits to write is greater than the current number of bits left
		else {
			//Isolates the number of bits we can still write in the far right into a new variable
			uint8_t bitsToWriteIncomplete = bits >> (num_bits_to_write - ((a_writer) -> num_bits_left));
		
			//Isolates the number(s) that could not be passed on to the current byte to the left
			uint8_t bitsLeft = bits << (8 + (a_writer -> num_bits_left) - num_bits_to_write);

			//Updates the current bytes variable using the bitsToWriteIncomplete  
			a_writer -> current_byte = bitsToWriteIncomplete | (a_writer -> current_byte);	

			//Copy this variabls so we can use it later after flushing and resetiing
			uint8_t numBitsLeftCopy = a_writer -> num_bits_left; 

			//Call flush bit writer in order to print the new updated current byte when we have nore num_bits_left
			flush_bit_writer(a_writer);	

			//Updates a_writer with the bitsLeft now that it was reset as well as its num left
			a_writer -> current_byte = (a_writer -> current_byte) | bitsLeft;

			//write_bits(a_writer, bitsLeft,num_bits_to_write - numBitsLeftCopy);
		
			//the number of bits left will be updated 
			a_writer -> num_bits_left = (a_writer->num_bits_left) - num_bits_to_write + numBitsLeftCopy; 
		}
	}
	

	assert(a_writer->num_bits_left > 0 && a_writer->num_bits_left <=8); 
}

//Call flush when num_bits_left is zero
void flush_bit_writer(BitWriter* a_writer) {
	//fwrite((*a_writer) -> current_byte, sizeof(a_writer ->current_byte), 1, a_writer -> file);
	if ((a_writer -> num_bits_left) != 8)
	{
		fputc(a_writer -> current_byte, a_writer -> file);
	}

	a_writer -> current_byte = 0;
	a_writer -> num_bits_left = 8;	
}

void close_bit_writer(BitWriter* a_writer) {
	flush_bit_writer(a_writer);
	fclose(a_writer -> file);
	(a_writer) -> file = NULL;

}



#define __BIT_WRITER_C_V1__
/* vim: set tabstop=4 shiftwidth=4 fileencoding=utf-8 noexpandtab colorcolumn=96: */
