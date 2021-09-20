#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 18:30:48 2021

@author: miguelcastilho
"""
################################################################################
# Author: Miguel Castilho
# Date: 02/26/2021
# This program will create a sum
# with the user inputs and an average of rain
###############################################################################

#eiufjkwnfjkklslkfklwnfwenwnf
years = int(input("Enter the number of years: "))

#If statements to check the year variable input
if years > 0:
    
    numberMonths = years * 12

    months = ["Jan", 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    count = 1

    totalRain = 0  

    #First for loop to iterate for every year
    for i in range(years):
    
        print(f"  For year No. {count}")
        
        
        x = months[0]
        
        msg = "    Enter the rainfall for " + x + ".: "
        
        rain = float(input(msg))
        
        count = count + 1
        
        totalRain += rain
        
        #Conditional to check if the rainfall isnt negative
        if rain < 0:
                print("Invalid input, please try again.")
                
                continue
                
        #For loop to iterate once for every year to add the necessary rainfall
        else:
            for j in range(1, 12):
        
                x = months[j]
        
                msg = "    Enter the rainfall for " + x + ".: "
        
                rain = float(input(msg))
                
                totalRain += rain
                
    
    avgRain = totalRain / numberMonths
    
    print(f"There are {numberMonths} months.")
    print(f"The total rainfall is {totalRain:0.2f} inches.")
    print(f"The monthly average rainfall is {avgRain:0.2f} inches.")
    
   


        
else:
    print("Invalid input.")
        
 
 
