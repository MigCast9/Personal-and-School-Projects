#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:19:33 2021

@author: miguelcastilho
"""
print('Enter the following quantities in feet.')
rowLength = float(input('  How long is this row? '))
endPostWidth = float(input('  How wide is the end-post assembly? '))
lineSpace = float(input('  How much space should be between the vines? '))

V = int((rowLength - 2 * endPostWidth)/lineSpace)
print('')
print(f'This row has enough space for {V} vine(s).')