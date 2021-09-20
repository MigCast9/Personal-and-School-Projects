################################################################################
# Author: Miguel C
# Date: 03/07/2021
# Description Says hello, better say it back!
################################################################################

# Don't change this
from turtle import *

def draw_e():
    # Write this function
    left(90)
    circle(40, 180)
    left(90)
    forward(80)
    right(180)
    forward(80)
    left(90)
    circle(40, 140)
    
    
def draw_h():
    # Write this function
    right(90)
    forward(120)
    left(180)
    forward(40)
    circle(-33, 180)
    forward(40)

def draw_l():
    # Write this function
    right(90)
    forward(120)

def draw_o():
    # Write this function
    circle(-40)
    

def draw_r():
    # Write this function
    right(90)
    forward(70)
    right(180)
    forward(48)
    circle(-27, 80)

def draw_t():
    # Write this function
    right(90)
    forward(120)
    left(180)
    forward(100)
    right(90)
    forward(27)
    right(180)
    forward(53)
    

def draw_u():
    # Write this function
    right(90)
    forward(27)
    circle(33,180)
    forward(27)
    right(180)
    forward(60)


def main():

    # Don't change this block --------------------------------------------------
    setup(600, 400)
    width(9)
    # --------------------------------------------------------------------------

    # Write your main function code here
    speed(9)
    #write the h
    penup()
    goto(-210, 190)
    pendown()
    draw_h()
    
    #write the e
    penup()
    goto(-30, 110)
    pendown()
    left(90)
    draw_e()
    
    #write the "l"s
    penup()
    goto(-5, 190)
    pendown()
    right(50)
    draw_l()
    
    penup()
    goto(40, 190)
    pendown()
    left(90)
    draw_l()
    
    #draw the o
    penup()
    goto(155, 110)
    pendown()
    draw_o()
    
    #draw the t
    penup()
    goto(-210,20)
    pendown()
    left(90)
    draw_t()
    
    #the u
    penup()
    goto(-150, -40)
    pendown()
    left(180)
    draw_u()
    
    #the r
    penup()
    goto(-60, -35)
    pendown()
    left(90)
    draw_r()
    
    #the t
    penup()
    goto(0,20)
    pendown()
    left(90)
    right(100)
    draw_t()
    
    #the l
    penup()
    goto(50, 20)
    pendown()
    left(180)
    draw_l()
    
    #e
    penup()
    goto(170, -60)
    pendown()
    left(90)
    draw_e()
    

# Don't change this
if __name__ == '__main__':
    main()
    done()
