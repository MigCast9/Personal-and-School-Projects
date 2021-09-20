################################################################################
# Author: Miguel Castilho Oliveira
# Date: 04/02/2021
# Description Statistics bruh, ever heard?
################################################################################
def main():
    filename = "rumpelstiltskin.txt"
    #Creates an empty list to input each line
    stringList = []
    with open(filename, "r") as fid:
        for line in fid:
            stringList.append(line.rstrip())    
    #This loop above appends to the empty list each line
    wordList = []
    count = 0
    for word in stringList:
        individualListWords = stringList[count].split()
        #This part above will transfrom every line in a list of strings, in which each elemnt is a word
        for i in range(len(individualListWords)):
            wordList.append(individualListWords[i])  
            #the loop above iterats through each item in the newly createdlist with words and appends them to another list
        count += 1
    #printing stuff down here
    lengthLines = len(stringList)
    lengthWords = len(wordList)
    print(f"Total number of words: {lengthWords}")
    print(f"Total number of lines: {lengthLines}")
    print(f"Average number of words per line:{lengthWords/lengthLines: .1f}")
    
if __name__ == '__main__':
    main()
