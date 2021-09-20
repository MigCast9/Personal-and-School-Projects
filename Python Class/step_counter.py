################################################################################
# Author: Miguel Castilho Oliveira
# Date: 04/02/2021
# Description This program is a step counter for a file that it reads provided by the course
################################################################################
    
def main():
    with open("steps.txt", 'r') as fid:
        allLines = fid.readlines()
    #Empty lists of the months to append
    jan = []
    feb = []
    mar= []
    apr= []
    may= []
    jun= []
    jul= []
    aug= []
    sep= []
    octo= [] #Comments, this is the list with all we need hurray
    nov= []
    dec= [] #Below is a crazy loop ye
    for i in range(31):
        jan.append(float(allLines[i].strip()))
    avgJan = sum(jan)/len(jan)
    for i in range(31, 59):
        feb.append(float(allLines[i].strip()))
    avgFeb = sum(feb)/len(feb)
    for i in range(59,90):
        mar.append(float(allLines[i].strip()))
    avgMar = sum(mar)/len(mar)
    for i in range(90,120):
        apr.append(float(allLines[i].strip()))
    avgApr = sum(apr)/len(apr)
    for i in range(120, 151):
        may.append(float(allLines[i].strip()))
    avgMay = sum(may)/len(may)
    for i in range(151,181):
        jun.append(float(allLines[i].strip()))
    avgJun = sum(jun)/len(jun)
    for i in range(181,212):
        jul.append(float(allLines[i].strip()))
    avgJul = sum(jul)/len(jul)
    for i in range(212, 243):
        aug.append(float(allLines[i].strip()))
    avgAug = sum(aug)/len(aug)
    for i in range(243,273):
        sep.append(float(allLines[i].strip()))
    avgSep = sum(sep)/len(sep)
    for i in range(273, 304):
        octo.append(float(allLines[i].strip()))
    avgOct = sum(octo)/len(octo)
    for i in range(304, 334):
        nov.append(float(allLines[i].strip()))
    avgNov = sum(nov)/len(nov)
    for i in range(334, 365):
        dec.append(float(allLines[i].strip()))
    avgDec = sum(dec)/len(dec)
    print("The average steps taken each month were:")
    print(f"   January : {avgJan:0.1f}")
    print(f"  February : {avgFeb:0.1f}")
    print(f"     March : {avgMar:0.1f}")
    print(f"     April : {avgApr:0.1f}")
    print(f"       May : {avgMay:0.1f}")
    print(f"      June : {avgJun:0.1f}")
    print(f"      July : {avgJul:0.1f}")
    print(f"    August : {avgAug:0.1f}")
    print(f" September : {avgSep:0.1f}")
    print(f"   October : {avgOct:0.1f}")
    print(f"  November : {avgNov:0.1f}")
    print(f"  December : {avgDec:0.1f}")
    #This part if the printing section to print all that is needed
if __name__ == '__main__':
    main()
