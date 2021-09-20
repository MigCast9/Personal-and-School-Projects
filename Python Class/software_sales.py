#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:32:21 2021

@author: miguelcastilho
"""
################################################################################
# Author: Miguel Castilho
# Date: 02/12/2021
# Calculate the final price for a package based on the discounts
#
################################################################################

Q = int(input('Please input the number of packages to be purchased: '))

if Q <= 0:
    print('  Invalid Input!')
    
elif Q<10:
    price = Q * 99
    print('  No discount applied.')
    print(f'  The final price for purchasing {Q} packages is ${price:,.2f}.')

elif 10 <= Q <= 19:
    price = Q * 99 * 0.9
    print('  10% discount applied.')
    print(f'  The final price for purchasing {Q} packages is ${price:,.2f}.')
    
elif 20 <= Q <= 49:
    price = Q * 99 * 0.75
    print('  25% discount applied.')
    print(f'  The final price for purchasing {Q} packages is ${price:,.2f}.')
          
elif 50<= Q <= 99:
    price = Q * 99 * 0.65
    print('  35% discount applied.')
    print(f'  The final price for purchasing {Q} packages is ${price:,.2f}.')
    
else:
    price = Q * 99 * 0.55
    print('  45% discount applied.')
    print(f'  The final price for purchasing {Q} packages is ${price:,.2f}.')