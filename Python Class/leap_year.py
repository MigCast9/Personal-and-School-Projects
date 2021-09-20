#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:28:10 2021

@author: miguelcastilho
"""

################################################################################
# Author: Miguel Castilho
# Date: 02/12/2021
# Leap year
#
################################################################################
year = int(input("Please input a year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print(f'In the year {year}, there are 29 days in February.')
    else:
        print(f"In the year {year}, there are 28 days in February.")
        

else:
    if year % 4 == 0:
        print(f'In the year {year}, there are 29 days in February.')
        
    else:
        print(f"In the year {year}, there are 28 days in February.")
        


