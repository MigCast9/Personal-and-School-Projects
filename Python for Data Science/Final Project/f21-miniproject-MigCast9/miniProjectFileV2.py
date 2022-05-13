import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge, Lasso
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import	linear_model
from sklearn.metrics import r2_score


def inputFunctionExcel(filename):

    files = pd.ExcelFile(filename)
    #Values for the Annual Averge Daily Traffic
    # Date = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Date'])
    Day = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Day'])
    highTemp = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['High Temp (°F)'])
    lowTemp = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Low Temp (°F)'])
    precipitation = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Precipitation'])
    brooklynBridge = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Brooklyn Bridge'])
    manhattanBridge = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Manhattan Bridge'])
    williamsburgBridge = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Williamsburg Bridge'])
    queensboroBridge = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Queensboro Bridge'])
    total = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Total'])
    
    dictOutput = {}
    
    # dictOutput.update({'Date':Date})
    dictOutput.update({'Day':Day})
    dictOutput.update({'highTemp':highTemp})
    dictOutput.update({'lowTemp':lowTemp})
    dictOutput.update({'precipitation':precipitation})
    dictOutput.update({'brooklynBridge':brooklynBridge})
    dictOutput.update({'manhattanBridge':manhattanBridge})
    dictOutput.update({'williamsburgBridge':williamsburgBridge})
    dictOutput.update({'queensboroBridge':queensboroBridge})
    dictOutput.update({'total':total})  

    return dictOutput

bikeDict = inputFunctionExcel('NYC_Bicycle_Counts_2016_Corrected.xlsx')

    
precipitationWrong = bikeDict['precipitation']
manhattanBridge = bikeDict['manhattanBridge']
brooklynBridge = bikeDict['brooklynBridge']
williamsburgBridge = bikeDict['williamsburgBridge']
queensboroBridge = bikeDict['queensboroBridge']
totalTraffic = bikeDict['total']

manhattanAVG = np.average(manhattanBridge)
brooklynAVG = np.average(brooklynBridge)
williamsburgAVG = np.average(williamsburgBridge)
queensboroAVG = np.average(queensboroBridge)
totalAVG = np.average(totalTraffic)
totalAvgDivided = totalAVG / 4

print('Manhattan Bridge:')
print(manhattanAVG)
print('Brooklyn Bridge:')
print(brooklynAVG)
print("Queensboro Bridge:")
print(queensboroAVG)
print('Williamsburg Bridge:')
print(williamsburgAVG)
print('Total Traffic:')
print(totalAvgDivided)


print('-----------------------------------------------------------------------')
print('Problem 2')

hightemp = bikeDict['highTemp']
lowtemp = bikeDict['lowTemp']
avgtemp = np.array([])
for iteration in range(len(hightemp)):
    step = ( hightemp[iteration] + lowtemp[iteration] ) /2
    avgtemp = np.append(avgtemp,step)
    
precipitation = []
for i in precipitationWrong:
    if i != 'T':
        precipitation.append(float(i))
    else:
        precipitation.append(0.01)

# print(10)

def main():
    #Importing dataset

    #Feature and target matrices
    X = np.array([precipitation, lowtemp, hightemp]).T
    y = totalTraffic
    #Training and testing split, with 25% of the data reserved as the test set
    # X = X.to_numpy()
    # y = y.to_numpy()
    [X_train, X_test, y_train, y_test] = train_test_split(X, y, test_size=0.25, random_state=101)

    #Normalizing training and testing data
    [X_train, trn_mean, trn_std] = normalize_train(X_train)
    X_test = normalize_test(X_test, trn_mean, trn_std)

    #Define the range of lambda to test
    lmbda = np.logspace(-1,2,num=51)#fill in
    # lmbda = [1,100]
    
    MODEL = []
    MSE = []
    for l in lmbda:
        #Train the regression model using a regularization parameter of l
        model = train_model(X_train,y_train,l)
        # print(model)

        #Evaluate the MSE on the test set
        mse = error(X_test,y_test,model)

        #Store the model and mse in lists for further processing
        MODEL.append(model)
        MSE.append(mse)
    #Plot the MSE as a function of lmbda
    #fill in
    plt.figure(1)
    plt.plot(lmbda, MSE)
    plt.xlabel("Lambda values")
    plt.ylabel("Mean Squared Errors")
    plt.title("MSE vs Lambda")
    
    #Find best value of lmbda in terms of MSE
    ind = MSE.index(min(MSE)) #fill in
    
    [lmda_best,MSE_best,model_best] = [lmbda[ind],MSE[ind],MODEL[ind]]

    print('Best lambda tested is ' + str(lmda_best) + ', which yields an MSE of ' + str(MSE_best))
    y_pred	= model_best.predict(X_test)
    
    print(r2_score(y_pred, y_test))

    return model_best


#Function that normalizes features in training set to zero mean and unit variance.
#Input: training data X_train
#Output: the normalized version of the feature matrix: X, the mean of each column in
#training set: trn_mean, the std dev of each column in training set: trn_std.
def normalize_train(X_train):

    #fill in
    X_train = np.array(X_train).transpose()
    std = []
    mean = []
    
    X = []
    
    for sideColumn in X_train:
        stdDevColumn = np.std(sideColumn)
        std.append(stdDevColumn)
        
        meanColumn = np.mean(sideColumn)
        mean.append(meanColumn)
        
        columnList = []
        for index in range(len(sideColumn)):
            # sideColumn[index] = (sideColumn[index] - meanColumn) / stdDevColumn
            columnList.append((sideColumn[index] - meanColumn) / stdDevColumn)
            
        X.append(columnList)    
    # X = X_train.T
    
    return np.array(X).T, np.array(mean), np.array(std)


#Function that normalizes testing set according to mean and std of training set
#Input: testing data: X_test, mean of each column in training set: trn_mean, standard deviation of each
#column in training set: trn_std
#Output: X, the normalized version of the feature matrix, X_test.
def normalize_test(X_test, trn_mean, trn_std):
    
    X = []
    #fill in
    X_test = np.array(X_test).transpose()
    for sideColumnIndex in range(len(X_test)):
        
        columnList = []
        # print(trn_mean)
        # print(len(sideColumnIndex))
        for index in range(len(X_test[sideColumnIndex])):
            # sideColumn[index] = (sideColumn[index] - trn_mean[index]) / trn_std[index]
            columnList.append((X_test[sideColumnIndex][index] - trn_mean[sideColumnIndex]) / trn_std[sideColumnIndex])
        X.append(columnList) 
        
    # X = X_test.T
    return np.array(X).T



#Function that trains a ridge regression model on the input dataset with lambda=l.
#Input: Feature matrix X, target variable vector y, regularization parameter l.
#Output: model, a numpy object containing the trained model.
def train_model(X,y,l):

    #fill in
    # linear_model = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)),X.T), y)
    model = linear_model.Ridge(alpha = l, fit_intercept=True)
    # model.fit(X,y)
    model.fit(X,y)
    return model

#Function that calculates the mean squared error of the model on the input dataset.
#Input: Feature matrix X, target variable vector y, numpy model object
#Output: mse, the mean squared error
def error(X,y,model):

    #Fill in
    #model = model.to_numpy()
    #y_model = np.dot(X,model)
    #mse = mean_squared_error(y_model, y)
    y = np.array(y)
    predictY = model.predict(X)
    mse = np.mean((y-predictY)**2)
    return mse

if __name__ == '__main__':
    model_best = main()
    #We use the following functions to obtain the model parameters instead of model_best.get_params()
    print(model_best.coef_)
    print(model_best.intercept_)

