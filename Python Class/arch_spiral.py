#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 15:12:36 2021

@author: miguelcastilho
"""

###############################################################################
# Author: Miguel Castilho
# Date: 03/08/2021
# Description does the archmedean spiral with equations and turtle module
###############################################################################
import math as m
from turtle import *

def main():
    # Don't change this block -------------------------------------------------
    setup(564, 564)
    width('5')
    speed(10)
    # -------------------------------------------------------------------------
    thetaDegrees = 0
    
   

    # Write your mainline logic here ------------------------------------------
    x = 0
    y = 0
    goto(x,y)
    
    #while loop that first gets the accurate value of the anlg ein radians, 
    #then decides where the turtle should go in the coordinate, then it updates the value of theta
    while thetaDegrees <= 2160:
        thetaRadians = thetaDegrees * m.pi / 180
        
        x = (thetaDegrees / 10) * m.cos(thetaRadians)
        y = (thetaDegrees / 10) * m.sin(thetaRadians)
        
        pendown()
       
        goto(x, y)
        
        thetaDegrees += 1
    

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()
