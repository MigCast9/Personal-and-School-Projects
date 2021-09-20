################################################################################
# Author: Miguel Castilho Oliveira
# Date: 03/16/2021
# Description: this program has function to take an integer and then use that integer to see its multiples inside a lst
################################################################################

#function that accepts the number and the list 
def multiples_of(integer, listMultiples):
    
    trueList = []
    listTrash = []
    
    for i in range(len(listMultiples)):
        if listMultiples[i] % integer == 0:
            trueList.append(listMultiples[i])
        else:
            listTrash.append(listMultiples[i])
            
    return(trueList)        


def main():

    number_list = [19, 2940, -189, 10, 28, -58, 1, 85, 201, -15, 122, 799, 406]
    
    theListMultiple = multiples_of(7, number_list)

    print("Original list of numbers:")   
    print(number_list)
    print("Numbers in the list that are multiples of 7:")
    print(theListMultiple)
    

if __name__ == '__main__':
    main()
