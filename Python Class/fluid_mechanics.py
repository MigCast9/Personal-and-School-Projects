#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 19:01:02 2021

@author: miguelcastilho
"""

################################################################################
# Author: Miguel Castilho
# Date: 02/12/2021
# Reynolds
###############################################################################

velocity = float(input('Enter the velocity of water in the pipe: '))
diameter = float(input('Enter the pipe`s diameter: '))
temperature = float(input('Enter the temperature in °C as 5, 10, or 15: '))

if temperature == 5:
    viscosity = 1.49 * 10 ** (-6)
    
    Reynolds = (velocity * diameter)/viscosity
    
elif temperature == 10:
    viscosity = 1.31 * 10 ** (-6)
    Reynolds = (velocity * diameter)/viscosity
    
else:
    viscosity = 1.15 * 10 ** (-6)
    Reynolds = (velocity * diameter)/viscosity



print(f'The Reynolds number for flow at {velocity} m/s in a {diameter} m diameter pipe at {temperature}°C is {Reynolds}')