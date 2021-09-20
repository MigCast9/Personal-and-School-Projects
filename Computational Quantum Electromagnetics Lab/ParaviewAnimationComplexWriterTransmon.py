import math as m

def fileConverterNodeVectorScalar(filename):
    with open(filename, 'r') as fid:
      fileString = fid.readlines()

    correctFileFormat = []
    
    for line in range(len(fileString)):
        
        if ',' in fileString[line]:
            
            #The next two lines creates a list with the items on each line for every iteration of the outer loop
            strippedLine = fileString[line].strip()
            correctLine = strippedLine.split(',')
            
            #The inner loop ietrate through all the items in each line to properly output them to the correct array
            for i in range(len(correctLine)):
                correctFileFormat.append(str(correctLine[i]))
                
        else:
            correctFileFormat.append(str(fileString[line].strip()))
        
        # correctFileFormat.append('\n')
          
    return(correctFileFormat) #Function returns the data included as a parameter in a proper format for output

def complexNumberCreator(realImaginaryList):
    complexList = []
    
    for i in range(0, len(realImaginaryList), 2):
        realPart = realImaginaryList[i]
        imagPart = realImaginaryList[i  + 1]
        complexNumber = complex(float(realPart), float(imagPart))
        
        complexList.append(complexNumber)
     
    return(complexList)
    

scalarList = fileConverterNodeVectorScalar('transmon_scalarDataComplex2.csv')
vectorList = fileConverterNodeVectorScalar('transmon_vectorDataComplex2.csv')

complexScalarList = complexNumberCreator(scalarList)
complexVectorList = complexNumberCreator(vectorList)

#Beginning process of altering scalar data

phase = 0 #Phase value to be altered ############ALTER HERE WHEN NEEDED
currentLoop = 0

while phase <= (2 * m.pi):

    multiplier = m.e ** (phase * complex(0, 1))

    #The two loops below will create new lists with the altered complex values of the scalars and vectors (Each in their own list)
    alteredComplexScalars = [] #List with the actual python complex scalars multiplied by e^(i * phase)
    #This loop creates the above list with the modified complex numbers
    for j in range(len(complexScalarList)):
        alteredComplexScalars.append(multiplier * complexScalarList[j])
        
    alteredComplexVectors = []
    for j in range(len(complexVectorList)):
        alteredComplexVectors.append(multiplier * complexVectorList[j])
        
    
    #The loops below create the lists with only the real parts of the modified complex numbers for both scalars and vectors
    realScalarData = [] #Real part of the scalar after being multipled by e^(i * phase)
    for j in range(len(alteredComplexScalars)):
        realScalarData.append(alteredComplexScalars[j].real)
    
    realVectorData = []
    for j in range(len(alteredComplexVectors)):
        realVectorData.append(alteredComplexVectors[j].real)
    
    
    #FOLLOWING TWO LOOPS WORK FOR THE SCALAR PART
    #This loop creates a list with the absolute value of the modified real parts of the complex numbers
    absoluteRealScalarData = []
    for j in range(len(realScalarData)):
        absoluteRealScalarData.append(abs(realScalarData[j]))
        
    normalizationConstant = max(absoluteRealScalarData)
    
    plottedScalarData = []#List with the data that will be plotted
    #This loop will divide each value in the real scalar data list by the normalization constant and append the results into a new list
    for j in range(len(realScalarData)):
        plottedScalarData.append(realScalarData[j] / normalizationConstant)
    
    #FOLLOWING LOOPS WORK FOR THE VECTOR DATA ONLY
    
    normalizedVectorData = [] #Vector data that will be plotted
    
    for j in range(0, len(realVectorData), 3):
        xVector = realVectorData[j]
        yVector = realVectorData[j + 1]
        zVector = realVectorData[j + 2]
        
        vectorMagnitude = (xVector**2 + yVector**2 + zVector**2) ** 0.5
        
        vectorNormValue = 20 * m.log(vectorMagnitude, 10)
        
        xNormalizedValue = (xVector / vectorMagnitude) * vectorNormValue
        yNormalizedValue = (yVector / vectorMagnitude) * vectorNormValue
        zNormalizedValue = (zVector / vectorMagnitude) * vectorNormValue
        
        normalizedVectorData.append(xNormalizedValue)
        normalizedVectorData.append(yNormalizedValue)
        normalizedVectorData.append(zNormalizedValue)
    
    #We will now create new files for the vectors and scalars for the animation
    scalarFilename = 'transmonComplexScalars' + str(currentLoop) + '.csv'
    vectorFilename = 'transmonComplexVectors' + str(currentLoop) + '.csv'
    
    with open(scalarFilename, 'w') as fid:
        for j in range(len(plottedScalarData)):
            fid.write(str(plottedScalarData[j]) + '\n')
    
    with open(vectorFilename, 'w') as fid:
        for j in range(0, len(normalizedVectorData), 3):
            fid.write(str(normalizedVectorData[j]) + ',')
            fid.write(str(normalizedVectorData[j + 1]) + ',')
            fid.write(str(normalizedVectorData[j + 2]) + '\n')
            
    phase += m.pi / 120
    currentLoop += 1
    
    