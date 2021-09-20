#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 22:54:07 2021

@author: miguelcastilho
"""

print('Please enter the following quantities.')
initialAmount = float(input('  How much is the initial deposit? '))
interestPercentage = float(input('  What is the annual interest rate in percent? '))
n = float(input('  How many times per year is the interest compounded? '))
time = float(input('  How many years will the account be left to earn interest? '))

interestRate = interestPercentage / 100

futureValue = initialAmount * (1 + (interestRate/n)) ** (n * time)


print('')
print(f'At the end of {time} years, the account will be worth ${futureValue:,.2f}.')