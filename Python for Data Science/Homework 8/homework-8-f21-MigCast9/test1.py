#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 16:41:39 2021

@author: miguelcastilho
"""
filename = 'english.txt'

def get_formatted_text(filename) :
    #fill in
    lines = []
    
    with open(filename, 'r') as fid:
        file = ["__" + line.strip().lower() + "__" for line in fid.readlines()]
    
    return file


def get_ngrams(line) :
    #fill in
    # ngrams = []
    # for character in range(2, len(line)):
    #     ngrams.append(line[character - 2] + line[character - 1] + line[character])
    
    ngrams = [line[character - 2] + line[character - 1] + line[character] for character in range(2, len(line))]
    return ngrams

# print(get_formatted_text(filename))
# print(get_formatted_text(filename)[0])
# print(get_ngrams(get_formatted_text(filename)[0]))

#Arguments:
#  filename: the filename to create an n-gram dictionary for
#Returns: a dictionary
#  where ngrams are the keys and the count of that ngram is the value.
#Notes: Remember that get_formatted_text() gives you a list of lines, and you want the ngrams from
#       all the lines put together.
#       You should use get_formatted_text() and get_ngrams() in this function.
#Hint: dict.fromkeys(l, 0) will initialize a dictionary with the keys in list l and an
#      initial value of 0
def get_dict(filename):
    #fill in
    ngram_dict = {}
    
    #lineString is a list of the lines present
    lineString = get_formatted_text(filename)
    
    #iterate through each line
    for line in lineString:
        
        #for each line, we grab a list of the ngrams present in each line
        ngramsLine = get_ngrams(line)
        
        #for each ngram present in the ngram list for each line, we add them to the dictionary if they weren't there. If they were already there, we alter the key's value
        for ngram in ngramsLine:
            if ngram in ngram_dict:
                ngram_dict[ngram] += 1
            else:
                ngram_dict.update({ngram:1})
    
    return ngram_dict

# print(get_dict(filename))
#Arguments:
#   filename: the filename to generate a list of top N (most frequent n-gram, count) tuples for
#   N: the number of most frequent n-gram tuples to have in the output list.
#Returns: a list of N tuples 
#   which represent the (n-gram, count) pairs that are most common in the file.
#   To clarify, the first tuple in the list represents the most common n-gram, the second tuple the second most common, etc...
#You may find the following StackOverflow post helpful for sorting a dictionary by its values: 
#Also consider the dict method popitem()
#https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
def top_N_common(filename,N):
    dicti = sorted(get_dict(filename).items(), key=lambda kv: kv[1])[::-1]
    common_N = [(dicti[key]) for key in range(N)]
    return common_N

#Arguments:
#   filenames_list: a list of filepath strings for the different language text files to process
#Returns: a list of dictionaries 
#   where each dictionary corresponds to one of the filepath strings.
#   Each dictionary in the list
#   should have keys corresponding to the n-grams, and values corresponding to the count of the n-gram
#Hint: Use functions defined in previous step.
def get_all_dicts(filenames_list):
    lang_dicts = [get_dict(filename) for filename in filenames_list]
    return lang_dicts

#Arguments:
#   list_of_dicts: A list of dictionaries where the keys are n-grams and the values are the count of the n-gram
#Returns: an alphabetically sorted list containing all of the n-grams across all of the dictionaries in list_of_dicts (note, do not have duplicates n-grams)
#Notes: It is recommended to use the "set" data type when doing this (look up "set union", or "set update" for python)
#   Also, for alphabetically sorted, we mean that if you have a list of the n-grams altogether across all the languages, and you call sorted() on it, that is the output we want
def dict_union(list_of_dicts):
    
    list_of_sets = [set(dictionary) for dictionary in list_of_dicts]
    union_ngrams = set().union(list_of_sets)
    
    return union_ngrams
