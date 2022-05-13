#_________________________________________
# VARIABLES
#
# CURRENT ASSIGNMENT
ASG_NICKNAME = HW21
BASE_NAME = huffman
#
# EXECUTABLES
EXECUTABLE = test_huffman
EXECUTABLE_GCOV = $(EXECUTABLE)_gcov

# SOURCE FILENAMES
SRC_C = huffman.c priority_queue.c bit_writer.c frequencies.c
TEST_C = test_huffman.c
SRC_H = huffman.h priority_queue.h bit_writer.h frequencies.h clog.h miniunit.h
SUBMIT_FILES = $(SRC_C) $(TEST_C) $(SRC_H) Makefile
#
# SYSTEM
SHELL = /bin/bash
CC = gcc
CFLAGS = -g -std=c11 -Wall -Wshadow -Wvla -Werror -pedantic
CFLAGS_GCOV = $(CFLAG) -fprofile-arcs -ftest-coverage
#__________________________________________
# RULES
$(EXECUTABLE): $(SRC_C) $(TEST_C) $(SRC_H) 
	$(CC) -o $(EXECUTABLE) $(SRC_C) $(TEST_C) $(CFLAGS)

test: $(EXECUTABLE)
	./$(EXECUTABLE)
	valgrind ./$(EXECUTABLE)

submit: 
	264submit $(ASG_NICKNAME) $(SUBMIT_FILES)

pretest: submit
	264test $(ASG_NICKNAME) 

clean:
	rm -f $(EXECUTABLE) *.gcov *.gcda *.gcno *_gcov

coverage: $(SRC_C) $(TEST_C)
	$(CC) -o $(EXECUTABLE_GCOV) $(SRC_C) $(TEST_C) $(CFLAGS_GCOV)
	./$(EXECUTABLE_GCOV)
	gcov -f $(SRC_C)

.PHONY: submit test pretest clean coverage

