################################################################################
# Author: Miguel Castilho Oliveira
# Date: 03/16/2021
# Description PIPOPOPOPOPIPOPOOIPIPIPPIPIPIPIPOPPOPPOPOPOPOIPIPOI
################################################################################
import random as r

def roll_d6():
    randomDice = r.randrange(1,7)
    return(randomDice)
#m fm,nwkjcnms cjkabsvk m,v avv mv jenvwe v
def get_2d6_rolls(numRolls):
    listRolls = []
    for i in range(numRolls):
        rollResult1 = roll_d6()
        rollResult2 = roll_d6()
        total = rollResult2 + rollResult1
        listRolls.append(total)
    return(listRolls)

def main():
    totalNumberOfRolls = 900000
    appearance2 = 0
    appearance3 = 0
    appearance4 = 0 
    appearance5 = 0
    appearance6 = 0
    appearance7 = 0
    appearance8 = 0
    appearance9 = 0
    appearance10 = 0
    appearance11= 0
    appearance12 = 0        
    theListRolls = get_2d6_rolls(totalNumberOfRolls)
    #iebfkjbwjfnewkjnfuwfkjwnfjkwnfiuwhfnwlkfwlfnuwnfnf
    for i in range(totalNumberOfRolls):
        
        if theListRolls[i] == 2:
            appearance2 += 1
            
        elif theListRolls[i] == 3:
            appearance3 += 1
            
        elif theListRolls[i] == 4:
            appearance4 += 1
        
        elif theListRolls[i] == 5:
            appearance5 += 1
            
        elif theListRolls[i] == 6:
            appearance6 += 1
            
        elif theListRolls[i] == 7:
            appearance7 += 1
            
        elif theListRolls[i] == 8:
            appearance8 += 1
            
        elif theListRolls[i] == 9:
            appearance9 += 1
            
        elif theListRolls[i] == 10:
            appearance10 += 1
            
        elif theListRolls[i] == 11:
            appearance11 += 1
            
        elif theListRolls[i] == 12:
            appearance12 += 1
    #setingoeirnfnwfnwkfnqnfnjvn;kebv;kw;vkjnv;qn iunq    
    freq2 = 100 * appearance2 / totalNumberOfRolls
    freq3 = 100 * appearance3 / totalNumberOfRolls
    freq4 = 100 * appearance4 / totalNumberOfRolls
    freq5 = 100 * appearance5 / totalNumberOfRolls
    freq6 =100 *  appearance6 / totalNumberOfRolls
    freq7 = 100 * appearance7 / totalNumberOfRolls
    freq8 =100 *  appearance8 / totalNumberOfRolls
    freq9 =100 *  appearance9 / totalNumberOfRolls
    freq10 = 100 * appearance10 / totalNumberOfRolls
    freq11 = 100 * appearance11 / totalNumberOfRolls
    freq12 = 100 * appearance12 / totalNumberOfRolls
    n2 = 2
    n3 = 3
    n4 = 4
    n5 = 5
    n6 = 6
    n7 = 7
    n8 = 8
    n9 = 9
    n10 = 10
    n11 =11
    n12=12
    #jnjfnewjkfbwbfwfuwfbwfbwbffwbwbfbfwwf
    print("Roll  Frequency")
    print(f"{n2:3d} {freq2:8.2f}%")
    print(f"{n3:3d} {freq3:8.2f}%")
    print(f"{n4:3d} {freq4:8.2f}%")
    print(f"{n5:3d} {freq5:8.2f}%")
    print(f"{n6:3d} {freq6:8.2f}%")
    print(f"{n7:3d} {freq7:8.2f}%")
    print(f"{n8:3d} {freq8:8.2f}%")
    print(f"{n9:3d} {freq9:8.2f}%")
    print(f"{n10:3d} {freq10:8.2f}%")
    print(f"{n11:3d} {freq11:8.2f}%")
    print(f"{n12:3d} {freq12:8.2f}%")


if __name__ == '__main__':
    main()
