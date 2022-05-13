from helper import remove_punc
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import numpy as np
import math as m

#Clean and stem the contents of a document
#Takes in a file name to read in and clean
#Return a list of words, without stopwords and punctuation, and with all words stemmed
# NOTE: Do not append any directory names to doc -- assume we will give you
# a string representing a file name that will open correctly
def read_and_clean_doc(doc) :
    #1. Open document, read text into *single* string
    with open(doc, 'r') as fid:
        docString = fid.read()
    #2. Tokenize string using nltk.tokenize.word_tokenize
    docString = nltk.word_tokenize(docString)
    #3. Filter out punctuation from list of words (use remove_punc)
    docString = remove_punc(docString)
    #4. Make the words lower case
    docString = [word.lower() for word in docString]
    #5. Filter out stopwords
    docString = [word for word in docString if word not in stopwords.words('english')]
    #6. Stem words
    stemmer = PorterStemmer()
    docString = [stemmer.stem(word) for word in docString]
    return docString
    
#Builds a doc-word matrix for a set of documents
#Takes in a *list of filenames*
#
#Returns 1) a doc-word matrix for the cleaned documents
#This should be a 2-dimensional numpy array, with one row per document and one 
#column per word (there should be as many columns as unique words that appear
#across *all* documents. Also, Before constructing the doc-word matrix, 
#you should sort the wordlist output and construct the doc-word matrix based on the sorted list
#
#Also returns 2) a list of words that should correspond to the columns in
#docword
def build_doc_word_matrix(doclist) :
    #1. Create word lists for each cleaned doc (use read_and_clean_doc)
    # wordlist = [sorted(read_and_clean_doc(doc)) for doc in doclist]  
    wordlist = sorted(list(set().union(*[sorted(read_and_clean_doc(doc)) for doc in doclist]  )))

    #2. Use these word lists to build the doc word matrix
    
    #We initialize docwords as a matrix of zeroes with the files as the rows and words as columns
    docword = np.zeros(((len(doclist), len(wordlist))))
    
    #Here we will loop throough the files, then for each file loop through the words 
    #and identify how many of each word exists in each file utilizing the first function
    for row in range(len(doclist)):
        for word in range(len(wordlist)):
            #Here in this next line we count how many of each word appear in each file. For that, we use the list obtained with the first function
            #, in which we get the file observed in the current iteration
            numWordsInFile = read_and_clean_doc(doclist[row]).count(wordlist[word])
            docword[row][word] = numWordsInFile
        
    return docword,sorted(wordlist)
    
#Builds a term-frequency matrix
#Takes in a doc word matrix (as built in build_doc_word_matrix)
#Returns a term-frequency matrix, which should be a 2-dimensional numpy array
#with the same shape as docword
def build_tf_matrix(docword) :
    #fill in
    tf = np.array([[wordNum / sum(wordCountLine) for wordNum in wordCountLine] for wordCountLine in docword])
    
    return tf
    
#Builds an inverse document frequency matrix
#Takes in a doc word matrix (as built in build_doc_word_matrix)
#Returns an inverse document frequency matrix (should be a 1xW numpy array where
#W is the number of words in the doc word matrix)
#Don't forget the log factor!
def build_idf_matrix(docword):
    #fill in
    idf = []
        
    for index,words in enumerate(docword.T):
        docOccurences = 0
        for ind, count in enumerate(words):
            if count != 0:
                docOccurences += 1
        logRes = m.log10(len(docword)/docOccurences)
        idf.append(logRes)
                
    idf = np.array(idf)    
    return idf.reshape(1,-1)

    # #The tf matrix will 
    # tf_matrix = build_tf_matrix(docword)
    # # print(tf_matrix)
    # # print(tf_matrix.shape())
    # idf = np.zeros((1, len(tf_matrix[0])))

    # for row in range(len(tf_matrix)):
    #     for word in range(len(tf_matrix[row])):
    #         if tf_matrix[row][word] != 0:
    #             idf[word] += 1
    
    
    
    # idf = [m.log(len(tf_matrix) / idf[i]) for i in range(len(idf))]

    # return idf
    
#Builds a tf-idf matrix given a doc word matrix
def build_tfidf_matrix(docword) :
    #fill in
    tf = build_tf_matrix(docword)
    idf = build_idf_matrix(docword)
    tfIDF = docword.copy()
    tfidf = np.array(tfIDF)
    for index,doc in enumerate(tf):
        for ind,term_frequency in enumerate(doc):
            result = idf[0][ind] * term_frequency
            tfidf[index][ind] = result  
    return tfidf
    
#Find the three most distinctive words, according to TFIDF, in each document
#Input: a docword matrix, a wordlist (corresponding to columns) and a doclist 
# (corresponding to rows)
#Output: a dictionary, mapping each document name from doclist to an (ordered
# list of the three most common words in each document
def find_distinctive_words(docword, wordlist, doclist) :
    #fill in
    #you might find numpy.argsort helpful for solving this problem:
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html
    distinctive_words = {}
    tfidf = build_tfidf_matrix(docword)
    
    for doc in range(len(tfidf)):
        indexesInverse = np.argsort(tfidf[doc])[::-1]
        distinctive_words.update({doclist[doc]:[wordlist[indexesInverse[0]],wordlist[indexesInverse[1]],wordlist[indexesInverse[2]]]})
   
    return distinctive_words

if __name__ == '__main__':
    from os import listdir
    from os.path import isfile, join, splitext
    
    ### Test Cases ###
    directory='lecs'
    path1 = join(directory, '1_vidText.txt')
    path2 = join(directory, '2_vidText.txt')
    
    # Uncomment and recomment ths part where you see fit for testing purposes
    
    print("*** Testing read_and_clean_doc ***")
    print(read_and_clean_doc(path1)[0:5])
    
    
    print("*** Testing build_doc_word_matrix ***") 
    doclist =[path1, path2]
    docword, wordlist = build_doc_word_matrix(doclist)
    print(docword.shape)
    print(len(wordlist))
    print(docword[0][0:10])
    print(wordlist[0:10])
    print(docword[1][0:10])
    
    print("*** Testing build_tf_matrix ***") 
    tf = build_tf_matrix(docword)
    print(tf[0][0:10])
    print(tf[1][0:10])
    print(tf.sum(axis =1))
    
    
    print("*** Testing build_idf_matrix ***") 
    idf = build_idf_matrix(docword)
    print(idf[0][0:10])
    
    
    print("*** Testing build_tfidf_matrix ***") 
    tfidf = build_tfidf_matrix(docword)
    print(tfidf.shape)
    print(tfidf[0][0:10])
    print(tfidf[1][0:10])
    
    print("*** Testing find_distinctive_words ***")
    print(find_distinctive_words(docword, wordlist, doclist))
    
