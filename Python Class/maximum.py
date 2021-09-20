#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:28:17 2021

@author: miguelcastilho
"""
################################################################################
# Author: Miguel Castilho
# Date: 02/27/2021
# This program will create a sum
# with the user inputs and an average
###############################################################################

#Defining the function
def max_of_two(first, second):
    
    if second > first:
        print(f"{second} is greater.")
        
        return(second)
        
    else:
        print(f"{first} is greater.")
        
        return(first)
        
#calling the function using main
def main():
    int1 = int(input("Enter the first integer: "))
    int2 = int(input("Enter the second integer: "))
    
    max_of_two(int1, int2)
    

