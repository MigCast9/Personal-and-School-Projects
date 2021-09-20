#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:05:17 2021

@author: miguelcastilho
"""
################################################################################
# Author: Miguel Castilho
# Date: 02/27/2021
# This program will create a sum
# with the user inputs and an average
###############################################################################

g = 9.81

#defini ghte fuctu=ion
def falling_distance(time):
    distance = (g * time ** 2) / 2
    
    return(distance)

#printing statements
print("Time (s)  Distance (m)")
print("----------------------")

#for loop to calculate the distance based on the time
for t in range(1, 11):
    theDistance = falling_distance(t)
    
    print(f"      {t:2.0f}" + f"       {theDistance: 7.2f}")