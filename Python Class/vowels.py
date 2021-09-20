###############################################################################
# Author: Miguel Castilho
# Date: 03/11/2021
# Description Draws the letter individually using turtle
###############################################################################

from turtle import *

#Individual functions for the letters
def draw_a():
    setheading(0)
    pendown()
    circle(-40, 450)
    forward(40)
    right(180)
    forward(80)
    penup()
    

#letter e jfekjwenfkw
def draw_e():
    setheading(0)
    pendown()
    left(90)
    circle(40, 180)
    left(90)
    forward(80)
    right(180)
    forward(80)
    left(90)
    circle(40, 140)
    penup()

#letter i fefbef
def draw_i():
    setheading(0)
    pendown()
    dot(10)
    penup()
    right(90)
    forward(30)
    pendown()
    forward(60)
    penup()
    

# letter o jkfnekjnfwknf
def draw_o():
    setheading(0)
    pendown()
    circle(-40)
    penup()
  

# letter u iuhwdw
def draw_u():
    setheading(0)
    pendown()
    right(90)
    forward(27)
    circle(33,180)
    forward(27)
    right(180)
    forward(60)
    penup()
    
#main function jbdnwv
def main():
    # You can use this for your own testing.
    draw_a()
    draw_e()
    draw_i()
    draw_o()
    draw_u()

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()