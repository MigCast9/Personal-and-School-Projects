################################################################################
# Author: Miguel C
# Date: 03/08/2021
# Description Does a star whohooo
################################################################################

# Don't change this
from turtle import *

#main function
def main():

    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()
    # --------------------------------------------------------------------------
    
    # Write your code here
    points = int(input("Enter number of points o star: "))
   
    
    innerAngle = int(360 / points)
    innerTurnAngle = 180 - innerAngle
    
    outerAngle = 2 * innerAngle
    outerTurnAngle = (180 - outerAngle) / 2
    
    gammaAngle = 180 - innerTurnAngle - innerAngle
    
    XAngle = outerAngle - 180 + gammaAngle
    
    color('black', 'red') 
    begin_fill()
    
    #for loop for the area
    
    
    right(outerTurnAngle)
    for i in range(1, points+1):
    
        forward(side_length)
        left(innerTurnAngle)
        forward(side_length)
        left(XAngle)
    
    # forward(side_length)
    # left(innerTurnAngle)
    # forward(side_length)
    # left(XAngle)
    # forward(side_length)
    # left(innerTurnAngle)
        
    goto(0, -side_length)
    end_fill()
   


# Don't change this
if __name__ == '__main__':
    main()
    done()
