#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 18:42:55 2021

@author: miguelcastilho
"""

################################################################################
# Author: Miguel Castilho
# Date: 02/12/2021
# Time calculator
###############################################################################

seconds = int(input("Please enter a time in seconds. "))

if seconds < 60:
    print("  The number of seconds is less than one minute.")
    
    
elif 60 <= seconds < 3600:
    minutes = int(seconds / 60)
    
    extraSeconds = seconds % 60
    
    print(f'  {seconds} seconds is: {minutes} minute(s) and {extraSeconds} second(s).')
    
elif 3600 <= seconds < 86400:
    
    hours = int(seconds / 3600)
    
    minutes = (int(seconds / 60) - (hours * 60))  
    
    extraSeconds = seconds % 60
    
    print(f'  {seconds: ,} seconds is: {hours} hour(s) {minutes} minute(s) and {extraSeconds} second(s).')
    

elif 86400 <= seconds:
    
    days = int(seconds / 86400)
    
    hours = int(seconds % 86400)/ 3600
    
    extraSeconds = seconds % 60
    
    minutes = extraSeconds // 60
    
    print(f'  {seconds: ,} seconds is: {days} day(s), {hours} hour(s), {minutes} minute(s) and {extraSeconds} second(s).')
    
    
    
    