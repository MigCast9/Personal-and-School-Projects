################################################################################
# Author: Miguel Castilho
# Date: 04/02/2021
# Description Writing numbers never felt so efficient (and so cool papi) DIOS MIO!
################################################################################
import random as r
def main():
    numbers = int(input("Enter the number of random numbers to be written to the file: "))
    randomNumberList = []
    for i in range(numbers):
        randomNumber = r.randrange(1, 501)
        randomNumberList.append(randomNumber)
    #Loop above generates one random number and adds it to a random number list every iteration
    
    with open('random_numbers.txt', 'w') as fid:
        for i in range(len(randomNumberList)):
            fid.write(str(randomNumberList[i]) + "\n")
if __name__ == '__main__':
    main()
