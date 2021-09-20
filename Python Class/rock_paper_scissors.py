###############################################################################
# Author: Miguel Castilho Oliveir
# Date: 03/11/2021
# Description: Rock paper scissors game wih user inputs and module
###############################################################################
import random as r
import math as m

def get_computer_choice():
    computerChoice = r.randrange(3)
    
    #coditionals based on random number generator
    if computerChoice == 0:
        return("rock")
    
    elif computerChoice == 1:
        return("paper")
    
    else:
        return("scissors")

def get_player_choice():
    
    userChoice = input("Choose rock, paper, or scissors: ")
                       
    while userChoice != "paper" and userChoice != "rock" and userChoice != "scissors":
        print("You made an invalid choice. Please try again.")
        userChoice = input("Choose rock, paper, or scissors: ")
        
    return(userChoice)
    
def get_winner(compChoice, myChoice):
    print("  The computer chose",compChoice,"and you chose",myChoice + ".")
    
    #selection structure
    if compChoice == myChoice:
        print("  Its a tie. Starting over.")
        return("tie")
    
    elif compChoice == "scissors" and myChoice == "paper":
        print("  scissors beats paper.")
        print("  You lost. Better luck next time.")
        print('Thanks for playing.')
        return("computer")
        
    elif compChoice == "scissors" and myChoice == "rock":
        print("  rock beats scissors.")
        print("  You won the game!")
        print('Thanks for playing.')
        return("player")
        
    elif compChoice == 'rock' and myChoice == "paper":
        print("  paper beats rock.")
        print("  You won the game!")
        print('Thanks for playing.')
        return("player")
    
    elif compChoice == 'rock' and myChoice == 'scissors':
        print("  rock beats scissors.")
        print("  You lost. Better luck next time.")
        print('Thanks for playing.')
        return("computer")
        
    elif compChoice == 'paper' and myChoice == "scissors":
         print("  scissors beats paper.")
         print("  You won the game!")
         print('Thanks for playing.')
         return("player")
     
    elif compChoice == 'paper' and myChoice == 'rock':
         print("  paper beats rock.")
         print("  You lost. Better luck next time.")
         print('Thanks for playing.')
         return("computer")
        
        
def main():
    # Write your mainline logic here ------------------------------------------
    
    #setting functions to the variables
    theCompChoice = get_computer_choice()
    theUserChoice = get_player_choice()
    
    #conditional strucutre
    if theCompChoice != theUserChoice:
        get_winner(theCompChoice, theUserChoice)
    
    
    else:
        #loop for ties
        while theCompChoice == theUserChoice:
             get_winner(theCompChoice, theUserChoice)
             theCompChoice = get_computer_choice()
             theUserChoice = get_player_choice()
             get_winner(theCompChoice, theUserChoice)
    

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
