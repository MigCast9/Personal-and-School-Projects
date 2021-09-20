################################################################################
# Author: Miguel Castilho Oliveira
# Date: 04/07/2021
# Description This function plots the covid cases in Indiana during the year
################################################################################
import matplotlib.pyplot as plt


def main():
    with open("indiana_covid_19_data.txt", 'r') as fid:
        fileData = fid.readlines()

    strippedFile = []
    for i in range(len(fileData)):
        strippedFile.append(fileData[i].strip())
        
    date = [] #first column
    
    newPositives = [] #third column
    
    totalPositives = [] #Total positives until said day
    for i in range(len(strippedFile)):
        lineList = strippedFile[i].split(" ")
        #Creating a list with the new positive cases for each day
        positivesDay = lineList[2]
        newPositives.append(float(positivesDay))
        
        #Creating a variable for the sum of the list of new positives for every day and appending each sum to the list with total positives for each day
        totalPositivesUntilDay = sum(newPositives)
        totalPositives.append(totalPositivesUntilDay)
        
        date.append(lineList[0])
    
    fig, ax = plt.subplots()
    ax.bar(date, totalPositives)
    ax.set_xticks([35, 96, 157, 218, 279, 341, 400 ])
    ax.set_xticklabels(['2020-03', '2020-05','2020-07','2020-09','2020-11','2021-01','2021-03'])
    ax.set_yticks([100, 200, 300, 400, 500, 600, 700])
    ax.set_ylabel("Number of Cases (in thousands)")
    ax.set_xlabel("Date")
    ax.set_title("Positive COVID-19 Cases in Indiana")
    
    
if __name__ == '__main__':
    main()
    plt.show()
