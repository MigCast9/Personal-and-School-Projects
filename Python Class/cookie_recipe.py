#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 23:22:01 2021

@author: miguelcastilho
"""



cookies = int(input('How many cookies do you want to make? '))

sugar = cookies * 0.03125

butter = (1 / 48) * cookies

flour = (2.75 / 48) * cookies

print(f'To make {cookies} cookies, you will need:')

print(f'{sugar: 7.2f} cups of sugar')
print(f'{butter: 7.2f} cups of butter')
print(f'{flour: 7.2f} cups of flour')