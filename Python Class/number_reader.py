################################################################################
# Author: Miguel Castilho Oliveira
# Date: 04/02/2021
# Description reads numbers majestically god bless. It creates arrays and lists and reads very well
################################################################################
    
def main():
    with open("random_numbers.txt", 'r') as fid:
        numberRaw = fid.readlines()
    
    #Creating the loop we need to have the necessary list
    listNew = []
    for i in range(len(numberRaw)):
        numStrip = numberRaw[i].strip()
        listNew.append(float(numStrip))
    
    #Using the list we crated to find what we need
    sumNum = int(sum(listNew))
    listNew.sort()
    maxNum = int(listNew[-1])
    minNum = int(listNew[0])
    avgNum = sumNum / len(listNew)
    #Printing statements yeah
    print(f"{len(listNew):,} numbers were read from the file.")
    print(f"Max: {maxNum:}")
    print(f"Min: {minNum:}")
    print(f"Sum: {sumNum:,}")
    print(f"Avg: {avgNum:0.1f}")
        


if __name__ == '__main__':
    main()
