################################################################################
# Author: Miguel Castilho Oliveira
# Date: 04/21/21
# Description Program for the dice and their outputs
################################################################################
import random as r

class Dice:
    """Creates a die"""
    
    def __init__(self, sides):
        """Initialize sides attributes"""
        self.sides = sides
    #Creating method for random side of the die after a single roll
    def roll(self):
        randomRoll = r.randrange(1, self.sides + 1)
        return(randomRoll)
    
    #Method for series of random sides of the die after n rolls
    def n_rolls(self,n):
        for i in range(n):
            theRoll = self.roll()
            if (i == n-1):
                print(f'{theRoll}')
            else:
                print(f"{theRoll}, ", end = "")
        return()

def main():
    sixDie = Dice(6)
    tenDie = Dice(10)
    twentyDie = Dice(20)
    
    print("Rolling a 6 sided die 10 times: ", end = "")
    sixDie.n_rolls(10)
    
    print("Rolling a 10 sided die 10 times: ", end = "")
    tenDie.n_rolls(10)
    
    print("Rolling a 20 sided die 10 times: ", end = "")
    twentyDie.n_rolls(10)
    
if __name__ == '__main__':
    main()
