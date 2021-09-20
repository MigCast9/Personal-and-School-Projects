###############################################################################
# Author: Miguel Castilho Oliveira
# Date:04/21/2021
# Description This project is the final project for the class, a wheel of fortune
###############################################################################
import math as m
import random as r

def selectSentence(filename): #reads all of the lines from the phrases file and outputs them to a list. The function will then return a random line from that list 
    listLines = []
    with open(filename, 'r') as fid:
        for line in fid:
            listLines.append(line.strip())
    randNumber = r.randrange(len(listLines))
    randomLine = listLines[randNumber]
    return(randomLine) #random line is returned as a string
    
#Code to replace the string with underscores and return that
def underscoreString(textLine): #sentence in this case is the sentence read from the file
    listCharacters = []
    listUnderscore = []
    
    for i in range(len(textLine)):
        listCharacters.append(textLine[i])
    
    for j in range(len(listCharacters)):
        if (listCharacters[j] != "'" and listCharacters[j] != ' ' and listCharacters[j] != '-' and listCharacters[j] != '_' and listCharacters[j] != '!' and listCharacters[j] != "&"):
            listUnderscore.append("_")
        else:
            listUnderscore.append(listCharacters[j])
           
    return("".join(listUnderscore))
        
def spin_the_wheel():
    possibleValues = [500, 500, 500, 500, 500, 550, 600, 600, 600, 600, 650, 650, 650, 700, 700, 700,800, 900, 2500, 'BANKRUPT', 'BANKRUPT']
    listIndex = r.randrange(0,21)
    randValue = possibleValues[listIndex]
    
    return(randValue)

#when called, the function will merely display what is going on to the user
def displayAndNextStep(underscores, unusedVowels, unusedConsonants,currentMoney, currentRound):
    print(f':::::::::::::::::::::::::::::::::::::::::: ROUND {currentRound} of 4 ::')
    print(f':: {underscores:53s}::')
    print( '::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print(f'::   {unusedConsonants}   ::   {unusedVowels}   ::',str('$'+f'{currentMoney:,}').rjust(10,' '), '::')
    print( '::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print("What would you like to do?")
    print("  1 - Spin the wheel")
    print("  2 - Buy a vowel")
    print("  3 - Solve the puzzle")
    print("  4 - Quit the game")
    numberChoice = (input("Enter the number of your choice: "))
    while (numberChoice != str(1) and numberChoice != str(2) and numberChoice != str(3) and numberChoice != str(4)):
        print(f'{numberChoice} is an invalid choice.')
        numberChoice = (input("Enter the number of your choice: "))
    
    return(float(numberChoice)) #the number choice wil be used for a selection structure in MAIN to determine what will be done next

def optionOne(textLine, consonantsLeft, currentMoney):
    fortuneSpin = spin_the_wheel()
    
    if fortuneSpin == 'BANKRUPT':
        print('The wheel landed on BANKRUPT.') 
        print(f'You lost ${currentMoney:,}!')
        cash = 0 #if bankrupt the cash will be zero and the function will return nothing at the end
        consonant = '_'
        output = [consonant, cash] #the fact that no consonat was returned means the player got the bankrupt option, when that happens we will end the turn and update his new amount of money to 0
    else: #if the cash is not zero  it will request the user to pick a consonant, which then will be used to see if it exists in the phrase
        print(f'The wheel landed on ${fortuneSpin:,}.')
        
        textLine = textLine.lower()
        consonantsLeft = consonantsLeft.lower()
        
        consonant = input("Pick a consonant: ")
        
        if (consonant.isdigit() == False):
            consonant = consonant.lower()
            
        
        while (len(consonant.lower()) != 1 or consonant.lower() == 'a' or consonant.lower() == 'e' or consonant.lower() == 'i' or consonant.lower() == 'o' or consonant.lower() == 'u' or consonant.isdigit() == True or consonant == '$' or consonant == '@' or consonantsLeft.lower().count(consonant.lower()) == 0):
           if (consonant.isdigit() == True or consonant == '$' or consonant == "@"):
               print(f"The character {consonant.upper()} is not a letter.")
               consonant = input("Pick a consonant: ")
        
           elif (consonant.lower() == 'a' or consonant.lower() == 'e' or consonant.lower() == 'i' or consonant.lower() == 'o' or consonant.lower() == 'u'):
               print("Vowels must be purchased.")
               consonant = input("Pick a consonant: ")
               
           elif len(consonant.lower()) != 1:
               print("Please enter exactly one character.")
               consonant = input("Pick a consonant: ")
               
           else: #(consonantsLeft.lower().count(consonant) == 0):
               print(f'The letter {consonant.upper()} has already been used.')
               consonant = input("Pick a consonant: ")
               
        #Here, after checking if the input is a consonant, it checks if the consonant is actually present in the text string. If present it will output the consonant and the money gotten
        if consonant.lower() in textLine.lower():
            
            appearances = textLine.count(consonant)
            
            cash = appearances * fortuneSpin #cash gained in turn will be fortune spin times the appearances
            
            output = [consonant, cash]
            
            if appearances == 1:
                print(f"There is 1 {consonant.upper()}, which earns you ${appearances * fortuneSpin:,}.")
            else:
                print(f"There are {appearances} {consonant.upper()}'s, which earns you ${appearances * fortuneSpin:,}.")
        else:
            cash = 0
            output = [consonant, cash]
            print(f"I'm sorry, there are no {consonant.upper()}'s.")
    return(output) #index 0 is the consonant chosen by the user and index 1 is the amount of money the user now has
#Case 1: goes bankrupt, returns 0 money and consonant = '-'
#Case 2: finds the letter. Prints the necessary statement and returns the chosen consonant as wellas the amount of money gained    
#Case 3: selects consonant that is not there. Prints necessary statement and returns 0 money and the consonant chosen

def optionTwoBuyVowel(currentMoney, vowelsLeft, textLine):
    vowelsLeft = vowelsLeft.lower()
    textLine = textLine.lower()
    cash = currentMoney - 250
    
    vowel = input('Pick a vowel: ')
    
    if (vowel.isdigit() == False):
            vowel = vowel.lower()
    
    while (len(vowel.lower()) != 1 and vowel.lower() != 'a' and vowel.lower() != 'e' and vowel.lower() != 'i' and vowel.lower() != 'o' and vowel.lower() != 'u' or vowelsLeft.count(vowel) == 0):
        if (vowel.isdigit() == True or vowel == '$' or vowel == '@'):
            print(f"The character {vowel} is not a letter.")
            vowel = input('Pick a vowel: ').lower()
            
        elif (vowel.lower() == 'b' or vowel.lower() == 'c' or vowel.lower() == 'd' or vowel.lower() == 'f' or vowel.lower() == 'g' or vowel.lower() == 'h' or vowel.lower() == 'j' or vowel.lower() == 'k' or vowel.lower() == 'l' or vowel.lower() == 'm' or vowel.lower() == 'n' or vowel.lower() == 'p' or vowel.lower() == 'q' or vowel.lower() == 'r' or vowel.lower() == 's' or vowel.lower() == 't' or vowel.lower() == 'v' or vowel.lower() == 'w' or vowel.lower() == 'x' or vowel.lower() == 'y' or vowel.lower() == 'z'):
            print("Consonants cannot be purchased.")
            vowel = input('Pick a vowel: ').lower()
            
        elif (len(vowel) != 1):
            print("Please enter exactly one character.")
            vowel = input('Pick a vowel: ').lower()
    
        else: #(vowelsLeft.count(vowel) == 0):
             print(f"The letter {vowel.upper()} has already been purchased.")
             vowel = input('Pick a vowel: ').lower()
    
    if vowel in textLine:
        appearances = textLine.count(vowel)
        print(f"There are {appearances} {vowel.upper()}'s.")
        
    
    else:
        print(f"I'm sorry, there are no {vowel.upper()}'s.")
       
        
    return(vowel) #returns the new amount of cash for index 1 and the vowel chosen so we can update the vowels left
    
def optionThreeSolvePuzzle(underscoreHiddenText, currentMoney, textLine):
        print("Enter your solution.")
        print(f"Clues: {underscoreHiddenText}")
        guess = input('Guess: ')
        
        if guess == textLine:
            print("Ladies and gentlemen, we have a winner!")
            print(f'You earned ${currentMoney:,d} for this round.')
            result = 'win'
        
        else:
            print("I'm sorry. The correct solution was:")
            print(f'{textLine.upper()}')
            print("You earned $0 this round")
            result = 'lose'
        return(result)    
        
    
# def optionFourQuitGame(cashOverFourRounds):
#     print("You earned $0 this round.")
#     print("Thanks for playing!")
#     print(f"You earned a total of ${cashOverFourRounds:,}.")
    #cash for the round will be zero

def transformHiddenText(hiddenText, phraseLine, letter): #letter can be a consonant or a vowel
    phraseLine = phraseLine.lower()
    phraseList = [] #creates list with every letter and space in the sentence
    
    letter = letter.lower()
    
    hiddenTextList = [] # creates list with every underscore in the sentence
    
    for i in range(len(phraseLine)):
        phraseList.append(phraseLine[i])
     
    for i in range(len(hiddenText)):
        hiddenTextList.append(hiddenText[i])
    
    
    
    
    for i in range(len(phraseList)):        
        if phraseList[i] == letter:
            hiddenTextList[i] = letter
            if (hiddenTextList[i - 1] == " "):
                letter = letter.upper()
            if hiddenTextList[i - 1] == "-":
                letter = letter.upper()

            
    hiddenText = "".join(hiddenTextList)
    
    
    truetext = hiddenText.capitalize()
    
    return(truetext)    
    



def main():
    totalRoundCash = 0
    theRound = 1
    while theRound < 5:
    #TAB ALL THAT IS DOWN BELOW
        currentRound = theRound #round 1 or 2 or 3 or 4
            
        theSentence = selectSentence('phrases.txt') #new phrase will be selected each loop
        
        hiddenSentence = underscoreString(theSentence)   
        
        unusedVowels = "AEIOU" #unused vowels, consonants and current money for the round when it starts
        unusedConsonants = "BCDFGHJKLMNPQRSTVWXYZ"
        currentMoney = 0 
    
        while theSentence != hiddenSentence:
            
            chosenOption = displayAndNextStep(hiddenSentence, unusedVowels, unusedConsonants,currentMoney, currentRound)
            
            if chosenOption == 1: #in case the user wants to find consonants
                if unusedConsonants == "                     ":
                    print("There are no more consonants to choose.")
                
                else:
                    listCashConsonant = optionOne(theSentence, unusedConsonants, currentMoney)           
                    
                    consonant = listCashConsonant[0]
                    
                    currentMoney += listCashConsonant[1] 
                    
                    unusedConsonants = unusedConsonants.upper().replace(consonant.upper(), " ")
                
                if consonant == '_':
                    currentMoney = 0
                
                hiddenSentence = transformHiddenText(hiddenSentence, theSentence, consonant)
              
            
            elif chosenOption == 2: #in case the user =wants to find vowels
                if unusedVowels == "     ":
                    print('There are no more vowels to buy.')
                
                else:
            
                    if currentMoney >= 250:
                        vowel = optionTwoBuyVowel(currentMoney, unusedVowels, theSentence)
                        currentMoney -= 250
                        
                        unusedVowels = unusedVowels.upper().replace(vowel.upper(), " ")
                        
                        hiddenSentence = transformHiddenText(hiddenSentence, theSentence, vowel)
                        
                    else:
                        print("You need at least $250 to buy a vowel.")      
                
            elif chosenOption == 3:
                result = optionThreeSolvePuzzle(hiddenSentence, currentMoney, theSentence)
                if result == 'win':
                    break
                
                else:
                    currentMoney == 0
                    break  
                
                
            else:
                # optionFourQuitGame(totalRoundCash)
                print("You earned $0 this round.")   
                currentMoney = 0
                theRound = 4
                break
            
        theRound += 1
            
            
        totalRoundCash += currentMoney
            
    print("Thanks for playing!")
    print(f"You earned a total of ${totalRoundCash:,}.")
        
if __name__ == '__main__':
    main()
