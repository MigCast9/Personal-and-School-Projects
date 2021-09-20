#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 00:08:59 2021

@author: miguelcastilho
"""
###############################################################################
# Author: Miguel Castilho Oliveira
# Date: 03/11/2021
# Description: Creates a math quiz using the random module and outputs whether the user has put the correct result
###############################################################################
import math as m
import random as r

#the random number generator
def random_number(digits):
    
    if digits == 2:
        
        number = r.randrange(10,100)
        
    else:
        number = r.randrange(100, 1000)
    
    return(number)

#main function
def main():
    # Write your mainline logic here ------------------------------------------
    twoDigitNumber = random_number(2)
    threeDigitNumber = random_number(3)
    
    #sum of the two random numbers
    result = threeDigitNumber + twoDigitNumber
    
    print(f'{twoDigitNumber: 5}')
    print(f'+{threeDigitNumber: 4}')
    print("-----")
    
    userAnswer = float(input("= "))
    
    if userAnswer == result:
        print("Correct -- Good Work!")
    else:
        print(f"Incorrect. The correct answer is {result}.")
    

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
