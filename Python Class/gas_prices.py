################################################################################
# Author: Miguel Castilho Oliveira
# Date: 04/7/2021
# Description plots the gas prices over the years 
################################################################################
import matplotlib.pyplot as plt
def main():
    with open("2008_Weekly_Gas_Averages.txt", 'r') as fid:
        lines = fid.readlines()
    #Setting lissts necessary to the output
    listAverages = []
    listWeeks = list(range(1,53))
    
    for line in range(len(lines)):
        listAverages.append(float(lines[line]))
    #Plotting the figure with everything that is asked
    fig, ax = plt.subplots()
    ax.plot(listWeeks, listAverages)
    ax.set_title("2008 Weekly Gas Prices")
    ax.set_xlabel("Weeks (by number)")
    ax.set_ylabel("Average Price (dollars/gallon)")
    ax.grid()
    ax.set_xlim(1,52)
    ax.set_ylim(1.5, 4.25)
    #Finishing here the plotting stuff
    

if __name__ == '__main__':
    main()
    plt.show()
