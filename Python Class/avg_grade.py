#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:57:33 2021

@author: miguelcastilho
"""
################################################################################
# Author: Miguel Castilho
# Date: 02/27/2021
# This program will create a sum
# with the user inputs and an average
###############################################################################

#uses a loop to get score until it is correct
listScores = []

def get_valid_score():

    score = float(input("Enter a score: "))
    
    while score < 0 or score > 100:
        print("Invalid Input. Please try again.")
        score = float(input("Enter a score: "))
    
    listScores.append(score)
    
    return(score)


#determines the letter grade of the score
def determine_grade(score):
    
    if 90 <= score <=100:
        print(f"The letter grade for {score} is A.")
        return("A")
        
    elif 80<= score < 90:
        print(f"The letter grade for {score} is B.")
        return("B")
        
    elif 70<= score < 80:
        print(f"The letter grade for {score} is C.")
        return("C")
     
    elif 60<= score < 70:
        print(f"The letter grade for {score} is D.")
        return("D")
    
    else:
        print(f"The letter grade for {score} is F.")
        return("F")


#calculates the average of the scores
def calc_average(S1, S2, S3, S4, S5):
    
    avgScore = (S1 + S2 + S3 + S4 + S5) / 5
    
    return(avgScore)

#main function that uses all three functions above to get the necessary inputs and outputs
def main():
    score1 = get_valid_score()
    determine_grade(score1)
    
    score2 = get_valid_score()
    determine_grade(score2)
    
    score3 = get_valid_score()
    determine_grade(score3)
    
    score4 = get_valid_score()
    determine_grade(score4)
    
    score5 = get_valid_score()
    determine_grade(score5)
    
    averageScore = calc_average(score1, score2, score3, score4, score5)
    
    print(f"The average score is{averageScore: 1.2f}.")
    


