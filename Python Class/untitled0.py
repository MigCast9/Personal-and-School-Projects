# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Tue Apr 27 16:15:19 2021

# @author: miguelcastilho
# """
import random as r

# def selectSentence(filename): #reads all of the lines from the phrases file and outputs them to a list. The function will then return a random line from that list 
#     listLines = []
#     with open(filename, 'r') as fid:
#         for line in fid:
#             listLines.append(line.strip())
#     randNumber = r.randrange(len(listLines))
#     randomLine = listLines[randNumber]
#     return(randomLine)
    




# #Code to replace the string with underscores and return that
# def underscoreString(textLine): #sentence in this case is the sentence read from the file
#     listCharacters = []
#     listUnderscore = []
    
#     for i in range(len(textLine)):
#         listCharacters.append(textLine[i])
    
#     for j in range(len(listCharacters)):
#         if (listCharacters[j] != ' ' and listCharacters[j] != '-' and listCharacters[j] != '_' and listCharacters[j] != '!'):
#             listUnderscore.append("_")
#         else:
#             listUnderscore.append(listCharacters[j])
           
#     return("".join(listUnderscore))

# sentence = selectSentence('phrases.txt')
# print(sentence)
# und = underscoreString(sentence)
# print(und)
# print(len([500, 500, 500, 500, 500, 550, 600, 600, 600, 600, 650, 650, 650, 700, 700, 700,800, 900, 2500, 'BANKRUPT', 'BANKRUPT']))
# underscores = '______---------_______ _____'
# currentRound = 1
# cash = 0
# unusedVowels = 'AEIOU'

# print(f':::::::::::::::::::::::::::::::::::::::::: ROUND {currentRound} of 4 ::')
# print(f'::{underscores:>40s}              ::')
# print( '::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
# print(f'::   BCDFGHJKLMNPQRSTVWXYZ   ::   {unusedVowels}   ::     ${cash:5,d} ::')
# print( '::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')


# cash = 2950

# def spin_the_wheel():
#     possibleValues = [500, 500, 500, 500, 500, 550, 600, 600, 600, 600, 650, 650, 650, 700, 700, 700,800, 900, 2500, 'BANKRUPT', 'BANKRUPT']
#     listIndex = r.randrange(0,22)
#     randValue = possibleValues[listIndex]
    
#     return(randValue)
# currentMoney = 100
# consonantsLeft = "BCFGHJKLMNPQRSTVWXYZ"
# textLine = 'Falling Asleep In The Library'


# currentMoney = 500
# vowelsLeft = "AEOU"
    

# vowelsLeft = vowelsLeft.lower()
# textLine = textLine.lower()
# cash = currentMoney - 250

# vowel = input('Pick a vowel: ')

# if (vowel.isdigit() == False):
#         vowel = vowel.lower()

# while (vowel.lower() != 'a' and vowel.lower() != 'e' and vowel.lower() != 'i' and vowel.lower() != 'o' and vowel.lower() != 'u' or vowelsLeft.count(vowel) == 0):
#     if (vowel.isdigit() == True or vowel == '$'):
#         print(f"The character {vowel} is not a letter")
#         vowel = input('Pick a vowel: ').lower()
        
#     elif (vowel.lower() == 'b' or vowel.lower() == 'c' or vowel.lower() == 'd' or vowel.lower() == 'f' or vowel.lower() == 'g' or vowel.lower() == 'h' or vowel.lower() == 'j' or vowel.lower() == 'k' or vowel.lower() == 'l' or vowel.lower() == 'm' or vowel.lower() == 'n' or vowel.lower() == 'p' or vowel.lower() == 'q' or vowel.lower() == 'r' or vowel.lower() == 's' or vowel.lower() == 't' or vowel.lower() == 'v' or vowel.lower() == 'w' or vowel.lower() == 'x' or vowel.lower() == 'y' or vowel.lower() == 'z'):
#         print("Consonants cannot be purchased.")
#         vowel = input('Pick a vowel: ').lower()
        
#     elif (len(vowel) != 1):
#         print("Please enter exactly one character.")
#         vowel = input('Pick a vowel: ').lower()

#     else: #(vowelsLeft.count(vowel) == 0):
#          print(f"The letter {vowel.upper()} has already been purchased.")
#          vowel = input('Pick a vowel: ').lower()

# if vowel in textLine:
#     appearances = textLine.count(vowel)
#     print(f"There are {appearances} {vowel.upper()}'s.")
#     output = [vowel, cash]

# else:
#     print(f"I'm sorry, there are no {vowel.upper()}'s.")
#     output = [vowel, cash]
        
        
# print(output)
hiddenText = "________ ___________"
phraseLine = 'Academic Scholarship'
letter = 'a'



# def transformHiddenText(hiddenText, phraseLine, letter): #letter can be a consonant or a vowel
#     phraseLine = phraseLine.lower()
#     phraseList = [] #creates list with every letter and space in the sentence
    
#     letter = letter.lower()
    
#     hiddenTextList = [] # creates list with every underscore in the sentence
    
#     for i in range(len(phraseLine)):
#         phraseList.append(phraseLine[i])
     
#     for i in range(len(hiddenText)):
#         hiddenTextList.append(hiddenText[i])
    
    
    
    
#     for i in range(len(phraseList)):
#         print(i)
        
#         if phraseList[i] == letter:
#             hiddenTextList[i] = letter
     
#     hiddenText = "".join(hiddenTextList)
#     truetext = hiddenText.capitalize()
    
#     return(truetext)


transformHiddenText(hiddenText, phraseLine, letter)


        




