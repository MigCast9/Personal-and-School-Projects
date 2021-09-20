#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 18:20:09 2021

@author: miguelcastilho
"""

################################################################################
# Author: Miguel Castilho
# Date: 02/12/2021
# This program calculates the number
# of Purdue students of year 1869
################################################################################

theNumber = int(input('Please enter a pocket number: '))

if theNumber < 0 or theNumber > 36:
    print("  Invalid Input!")
    
elif theNumber == 0:
    print("  Pocket 0 is green.")
    
elif 1 <= theNumber <= 10:
    if theNumber % 2 == 0:
        print(f"  Pocket {theNumber} is black.")
    
    else:
        print(f"  Pocket {theNumber} is red.")
    
    
elif 11 <= theNumber <= 18:
     if theNumber % 2 == 0:
        print(f"  Pocket {theNumber} is red.")
    
     else:
        print(f"  Pocket {theNumber} is black.")
        
    
elif 19 <= theNumber <= 28:
    if theNumber % 2 == 0:
        print(f"  Pocket {theNumber} is black.")
    
    else:
        print(f"  Pocket {theNumber} is red.")
    
    
elif 29 <= theNumber <= 36:
   if theNumber % 2 == 0:
        print(f"  Pocket {theNumber} is red.")
    
   else:
        print(f"  Pocket {theNumber} is black.")