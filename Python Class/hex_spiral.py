################################################################################
# Author: Miguel C
# Date: 03/062021
# Description: does the hex spiral yay
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width('5')
    # --------------------------------------------------------------------------

    # Write your code here
    count = 6
    
    for i in range(39):
        forward(count)
        right(60)
        
        count += 6

# Don't change this
if __name__ == '__main__':
    main()
    done()
