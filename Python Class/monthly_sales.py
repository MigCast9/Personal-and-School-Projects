################################################################################
# Author: Miguel Castilho Oliveira
# Date: 04/07/2021
# Description Sales for each month ,therefore monthly sales. This code is superb
################################################################################
import matplotlib.pyplot as plt

def main():
    monthlySales = []
    
    monthList = ("January", "February", "March", "April","May","June","July","August","September","October","November","December")
    #Appends each input for every month on the sales list
    for month in range(len(monthList)):
        monthlySales.append(float(input("Enter the sales for "+ monthList[month] + ": " )))
    
    colors = ("#4D4038", "#BAA892", '#5B6870', "#6E99B4", "#A3D6D7", '#085C11', '#849E2A', '#C3BE0B', '#E9E45B', '#6B4536', '#B46012', '#FF9B1A')
    #part where we create the figure
    fig, ax = plt.subplots()
    ax.pie(monthlySales, colors = colors, labels = monthList)
    ax.set_title("Monthly Sales Values", )
    
if __name__ == '__main__':
    main()
    plt.show()
