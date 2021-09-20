################################################################################
# Author: Miguel Castilho Oliveira
# Date: 04/07/2021
# Description Graphs the sin and cos
################################################################################
import matplotlib.pyplot as plt
import math as m

def main():
    xAxis = list(range(0, 6284,1))
    xAxisTrue = [] #List with the correct values for the x axis
    for i in xAxis:
        trueValue = xAxis[i] / 1000
        xAxisTrue.append(trueValue) # This is appending the treu value of the x axis to the list since the normal range function is wickity wack yo
        
    sineList = []
    cosineList = []
    for i in range(len(xAxisTrue)):
        #Calculate the sine value for every x value and include the sine in its list
        sine = m.sin(xAxisTrue[i])
        sineList.append(sine)
        
        #Calculate the cosine value for every x value and include the sine in its list
        cosine = m.cos(xAxisTrue[i])
        cosineList.append(cosine)
    fig, ax = plt.subplots()
    ax.plot(xAxisTrue, sineList, color = 'r')
    ax.plot(xAxisTrue, cosineList, color = 'b')
    ax.set_xlim(0, 2 * m.pi)
    ax.set_ylim(-1,1)
    ax.set_xticks([m.pi/2 , m.pi, 3*m.pi/2, 2*m.pi])
    ax.set_xticklabels(["$\\pi/2$", "$\\pi$","$3\\pi/2$", "$2\\pi$"])
    ax.set_yticks([-1, 1])
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero')
    
    
        


if __name__ == '__main__':
    main()
    plt.show()
