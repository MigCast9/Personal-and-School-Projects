################################################################################
# Author: Miguel Castilho Oliveira
# Date: 03/16/2021
# Description: pipipipopopopopipipipopopopipipopopipoipoipoi
################################################################################

def get_number_list():
    #taking in inputs and adding to list
    n1 = float(input("  Enter number  1 of 10: "))
    n2 = float(input("  Enter number  2 of 10: "))
    n3 = float(input("  Enter number  3 of 10: "))
    n4 = float(input("  Enter number  4 of 10: "))
    n5 = float(input("  Enter number  5 of 10: "))
    n6 = float(input("  Enter number  6 of 10: "))
    n7 = float(input("  Enter number  7 of 10: "))
    n8 = float(input("  Enter number  8 of 10: "))
    n9 = float(input("  Enter number  9 of 10: "))
    n10 = float(input("  Enter number 10 of 10: "))
    #appending to the list
    theList = [n1, n2,n3,n4,n5,n6,n7,n8,n9,n10]
    return(theList)

def main():
#main function in which there is a calling function to call the function called
    listMain = get_number_list()
    listMain.sort()
    lowestNumber = listMain[0]
    biggestNumber = listMain[-1]
    total = sum(listMain)
    average = total / len(listMain)
    
    print(f"Lowest number: {lowestNumber:.2f}")
    print(f"Highest number: {biggestNumber:.2f}")
    print(f"Total: {total:.2f}")
    print(f"Average: {average:.2f}")

if __name__ == '__main__':
    main()
