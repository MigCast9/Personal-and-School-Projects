import numpy as np
import matplotlib.pyplot as plt

#Return fitted model parameters to the dataset at datapath for each choice in degrees.
#Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
#Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
#coefficients when fitting a polynomial of d = degrees[i].
def main(datapath, degrees):
    paramFits = []
    
    with open(datapath, 'r') as fid:
        lines = fid.readlines()
    samples = [i.strip().split(" ") for i in lines]
    x = []
    y = []

    for i in samples:
        x.append(float(i[0]))   
        y.append(float(i[1]))    
    
    for n in degrees:
        featureMatrix = feature_matrix(x, n)
        paramFits.append(least_squares(featureMatrix, y))
    
    #fill in
    #read the input file, assuming it has two columns, where each row is of the form [x y] as
    #in poly.txt.
    #iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    #for the model parameters in each case. Append the result to paramFits each time.
    Yvalues = []
    for polynomial in paramFits:
        powers = np.arange(len(polynomial)-1, -1, -1)
        yPolynomial = []
        
        for xSample in x:
            ySample = 0
            
            for index in range(len(powers)):
                ySample += (xSample ** powers[index]) * polynomial[index] 
            yPolynomial.append(ySample)
            
        Yvalues.append(yPolynomial)
        
    
    plt.figure(1)
    plt.scatter(x,y)
    for index in range(len(paramFits)):
        xPlot, yPlot = zip(*sorted(zip(x, Yvalues[index])))
        plt.plot(xPlot,yPlot, label = f'degree = {len(paramFits[index]) - 1}')
    plt.legend()

    return paramFits    

#Return the feature matrix for fitting a polynomial of degree d based on the explanatory variable
#samples in x.
#Input: x as a list of the independent variable samples, and d as an integer.
#Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
#for the ith sample. Viewed as a matrix, X should have dimension #samples by d+1.
def feature_matrix(x, d):
    X = []
    d = np.array(np.arange(d, -1, -1))
    # print(d)
    for sample in x:
        xList = []
        for degree in d:
            xList.append(sample ** degree)
        X.append(xList)   
    #print(X) 
    
    #fill in
    #There are several ways to write this function. The most efficient would be a nested list comprehension
    #which for each sample in x calculates x^d, x^(d-1), ..., x^0.
    #print(X)
    return X


#Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
#Input: X as a list of features for each sample, and y as a list of target variable samples.
#Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X = np.array(X)
    y = np.array(y)
    # print(y)
    B = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)),X.T), y)
    #fill in
    #Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.

    return B

if __name__ == '__main__':
    datapath = 'poly.txt'
     # degrees = [2, 4]
    # degrees = [1,2,3,4,5]
    degrees = [1,2,3,4,5]
    paramFits = main(datapath, degrees)
    print(paramFits)
