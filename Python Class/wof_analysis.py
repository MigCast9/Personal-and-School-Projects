###############################################################################
# Author: Miguel Castiho Oliveira
# Date: 04/29/2021
# Description Graphs the amount of each letter in the phrases file
###############################################################################
import matplotlib.pyplot as plt
def main():
    listLines = []
    listLetters = []
    totalLetters = 0
    with open('phrases.txt', 'r') as fid:
        for line in fid:
            listLines.append(line.strip())
    for i in range(len(listLines)): #This nested loop goes through each line individually and then gets the letters in the inner loop
        for j in range(len(listLines[i])):
            listLetters.append(listLines[i][j])
    totalLetters = len(listLetters)
    #now we append each letter, both upper and lower case into the respective variables
    a = (listLetters.count('a') + listLetters.count("A")) / totalLetters
    b = (listLetters.count('b') + listLetters.count("B")) / totalLetters
    c = (listLetters.count('c') + listLetters.count("C")) / totalLetters
    d = (listLetters.count('d') + listLetters.count("D")) / totalLetters
    e = (listLetters.count('e') + listLetters.count("E")) / totalLetters
    f = (listLetters.count('f') + listLetters.count("F")) / totalLetters
    g = (listLetters.count('g') + listLetters.count("G")) / totalLetters
    h = (listLetters.count('h') + listLetters.count("H")) / totalLetters
    i = (listLetters.count('i') + listLetters.count("I")) / totalLetters
    j = (listLetters.count('j') + listLetters.count("J")) / totalLetters
    k = (listLetters.count('k') + listLetters.count("K")) / totalLetters
    l = (listLetters.count('l') + listLetters.count("L")) / totalLetters
    m = (listLetters.count('m') + listLetters.count("M")) / totalLetters
    n = (listLetters.count('n') + listLetters.count("N")) / totalLetters
    o = (listLetters.count('o') + listLetters.count("O")) / totalLetters
    p = (listLetters.count('p') + listLetters.count("P")) / totalLetters
    q = (listLetters.count('q') + listLetters.count("Q")) / totalLetters
    r = (listLetters.count('r') + listLetters.count("R")) / totalLetters
    s = (listLetters.count('s') + listLetters.count("S")) / totalLetters
    t = (listLetters.count('t') + listLetters.count("T")) / totalLetters
    u = (listLetters.count('u') + listLetters.count("U")) / totalLetters
    v = (listLetters.count('v') + listLetters.count("V")) / totalLetters
    w = (listLetters.count('w') + listLetters.count("W")) / totalLetters
    x = (listLetters.count('x') + listLetters.count("X")) / totalLetters
    y = (listLetters.count('y') + listLetters.count("Y")) / totalLetters
    z = (listLetters.count('z') + listLetters.count("Z")) / totalLetters
    freqList = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
    listWidth =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    listWidthTrue = []
    for i in range(len(listWidth)):
        listWidthTrue.append(listWidth[i].upper()) 
    fig, ax = plt.subplots()
    ax.bar(listWidthTrue, freqList)
    ax.grid()
    ax.set_title("Letter Frequency in Puzzle Phrases")
    ax.set_xlabel('Letter')
    ax.set_ylabel('Letter Appearance Frequency')
    ax.set_ylim(0,0.10)
if __name__ == '__main__':
    main()
    plt.show()