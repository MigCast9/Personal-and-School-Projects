###############################################################################
# Author: Miguel Castilho
# Date: 03/11/2021
# Description Drwas the letters imported randomly
###############################################################################

from turtle import *

# Add your imports here -------------------------------------------------------
import vowels as v
import random as r


def main():
    # Don't change this block -------------------------------------------------
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)
    # -------------------------------------------------------------------------


    # Write your mainline logic here ------------------------------------------
    a = v.draw_a # letter a bewfbwf
    
    e = v.draw_e # letter e fjenwfinwf
    
    i = v.draw_i # letter i oenfowf
    
    o = v.draw_o # letter o jkfwenf
    
    u = v.draw_u # letter u kjnfwfnw
    
     #creates and shuffles the vowels list
    listVowels = [a, e, i ,o, u]
    r.shuffle(listVowels)
    
    locationX = -220
     #for loop to print out all of the letters yays
    for item in listVowels:
        goto(locationX, -30)
        
        item()
        
        locationX += 100

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main() # main function
    done()