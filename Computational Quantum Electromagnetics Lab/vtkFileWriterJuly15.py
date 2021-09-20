#This function will return the correct array that will be written in the VTK file
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
                correctFileFormat.append(str(correctLine[i]) + " ")
                
        else:
            correctFileFormat.append(str(fileString[line].strip()))
        
        correctFileFormat.append('\n')
          
   return(correctFileFormat) #Function returns the data included as a parameter in a proper format for output

def fileConverterPoygons(filename): #This function does the same thing as the function above for the Polygon/Cell indexing, which works a bit differently than the other data present in the file format
    
    with open(filename, 'r') as fid:
         fileString = fid.readlines()
         
    correctFileFormat = []
    
    
    for line in range(len(fileString)):
    
         strippedLine = fileString[line].strip()
                
         correctLine = strippedLine.split(',')
         
         #The following lines in the loop create the necessary format for the VTK file to read the cells. Firstly, the number of nodes for each cell is written, then, 
         #the indices of the nodes themselves are written. In sequence, the new line character is also written inside the list to make it easier to write later on.
         
         correctFileFormat.append(str(int(len(correctLine))) + " ")
       
         for i in range(int(len(correctLine))):
             correctFileFormat.append(str(int(correctLine[i]) - 1) + " ")
       
         correctFileFormat.append('\n')
              
    return(correctFileFormat)
    
#This function will return the number of lines in each datapool
def numberOfLines(filename):
    with open(filename, 'r') as fid:
       fileString = fid.readlines()
    numLines = len(fileString)
    
    return(numLines)

def numberOfItems(fileCorrectFormat):
    fileCorrectNumber = []
    for i in range(len(fileCorrectFormat)):
       if fileCorrectFormat[i] != '\n':
          fileCorrectNumber.append(fileCorrectFormat[i])        
     
    return(len(fileCorrectNumber)) #This function returns the number of items in a specific attribute of the file (LINES x ITEMS PER LINE)

#The main function will get the input, call the necessary functions and create the new VTK file as desired
def main():
    dataPointFile = input("Enter here the node data file: ")
    dataCellsFile = input("Enter here the file containing the cells: ")
    
    correctCells = fileConverterPoygons(dataCellsFile)
    
    dataScalarFile = input("Enter here the file containing the scalars (if none just press ENTER): ")
    dataVectorFile = input("Enter here the file containing the vectors (if none just press ENTER): ")
    datasetNum = int(input("If it's a 2D Surface only (POLYDATA) enter '1' and if it's a 3D visualization where the insides matter (UNSTRUCTURED_GRID) enter '2': "))

    vtkFirstLine = '# vtk DataFile Version 3.0\n'
    vtkHeader = 'VTK File created here'
    vtkASCII = '\nASCII\n'    
    
    # dataset = ''
    if datasetNum == 1:
        dataset = 'POLYDATA '
    elif datasetNum == 2:
        dataset = 'UNSTRUCTURED_GRID '
        print(' 1 - Vertex \n 2 - Poly Vertex \n 3 - Line \n 4 - Poly Line \n 5 - Triangle \n 6 - Triangle Strip \n 7 - Polygon \n 8 - Pixel \n 9 - Quad \n 10 - Tetrahedron \n 11 - Voxel \n 12 - Hexahedron \n 13 - Wedge \n 14 - Pyramid')
        unstrucCellChosen = int(input('Enter the number equivalent to the cell type present in your 3D mesh: '))
        
    vtkDesiredFormat = 'DATASET ' + dataset + '\n'
    
    if datasetNum == 1:
        cellType = 'POLYGONS'
    elif datasetNum == 2:
        cellType = 'CELLS'
    
    correctNodes = fileConverterNodeVectorScalar(dataPointFile)
    numNodes = numberOfLines(dataPointFile)
    
    numCells = numberOfLines(dataCellsFile)
    numItemsCells = numberOfItems(correctCells)
          
    vtkFileName = input("Enter here the name of your new file: ")
    with open(vtkFileName, 'w') as fid:
        fid.write(vtkFirstLine)
        fid.write(vtkHeader)
        fid.write(vtkASCII)
        fid.write(vtkDesiredFormat)
        #If there are no vectors and scalars, we write only the nodes and cells
        fid.write(f'\nPOINTS {numNodes} double \n')
        for i in range(len(correctNodes)):
            fid.write(correctNodes[i])
            
        fid.write(f'{cellType} {numCells} {numItemsCells} \n')
        for i in range(len(correctCells)):
            fid.write(correctCells[i])
        
        if datasetNum == 2:
            fid.write(f'CELL_TYPES {numCells} \n')
            for i in range(numCells):
                fid.write(f'{unstrucCellChosen} \n')
        
        if dataScalarFile == "" and dataVectorFile == "":  
            fid.close()
                
        elif dataScalarFile == "":
            #if there are vectors but no scalars, we write only the vectors
            print('Select the number that represents the data structure your vector data is attached to: \n 1 - Cells \n 2 - Points')
            dataStructureVector = int(input("Enter the number here for the: "))
            
            if dataStructureVector == 1:
                fid.write(f'CELL_DATA {numCells} \n')
                
            elif dataStructureVector == 2:
                fid.write(f'POINT_DATA {numNodes} \n')
                
            fid.write('VECTORS vectors double\n')
            correctVectors = fileConverterNodeVectorScalar(dataVectorFile)
            for i in range(len(correctVectors)):
                fid.write(correctVectors[i])
        
        elif dataVectorFile == "":
            #if there are no vectors but scalars are present we write
            print('Select the number that represents the data structure your scalar data is attached to: \n 1 - Cells \n 2 - Points')
            dataStructureScalar = int(input("Enter the number here: "))
            
            if dataStructureScalar == 1:
                fid.write(f'CELL_DATA {numCells} \n')
                
            elif dataStructureScalar == 2:
                fid.write(f'POINT_DATA {numNodes} \n')
            
            fid.write('SCALARS scalars double \n')
            fid.write('LOOKUP_TABLE tableScalar \n')
            correctScalars = fileConverterNodeVectorScalar(dataScalarFile)
            
            for i in range(len(correctScalars)):
                fid.write(correctScalars[i])

        else:
            #If both vectors and scalars are included the program writes it all
            print('Select the number that represents the data structure your scalar data is attached to: \n 1 - Cells \n 2 - Points')
            dataStructureScalar = int(input("Enter the number here: "))
            
            if dataStructureScalar == 1:
                fid.write(f'CELL_DATA {numCells} \n')
                
            elif dataStructureScalar == 2:
                fid.write(f'POINT_DATA {numNodes} \n')
            
            fid.write('SCALARS scalars double \n')
            fid.write('LOOKUP_TABLE tableScalar \n')
            correctScalars = fileConverterNodeVectorScalar(dataScalarFile)
            
            for i in range(len(correctScalars)):
                fid.write(correctScalars[i])
            
            print('Select the number that represents the data structure your vector data is attached to: \n 1 - Cells \n 2 - Points')
            dataStructureVector = input("Enter the number here: ")
            
            if int(dataStructureVector) == dataStructureScalar:
                fid.write('VECTORS vectors double\n')
                correctVectors = fileConverterNodeVectorScalar(dataVectorFile)
                for i in range(len(correctVectors)):
                    fid.write(correctVectors[i])
                
            elif dataStructureVector == '1' and dataStructureVector != str(dataStructureScalar):
                fid.write(f'CELL_DATA {numCells} \n')
                fid.write('VECTORS vectors double\n')
                correctVectors = fileConverterNodeVectorScalar(dataVectorFile)
                for i in range(len(correctVectors)):
                    fid.write(correctVectors[i])
                    
            elif dataStructureVector == '2' and dataStructureVector != str(dataStructureScalar):
                fid.write(f'POINT_DATA {numNodes} \n')
                fid.write('VECTORS vectors double\n')
                correctVectors = fileConverterNodeVectorScalar(dataVectorFile)
                for i in range(len(correctVectors)):
                    fid.write(correctVectors[i])
    
            # correctVectors = fileConverterNodeVectorScalar(dataVectorFile)
            # correctScalars = fileConverterNodeVectorScalar(dataScalarFile)
            
            # fid.write(f'CELL_DATA {numCells} \n')
            # fid.write('SCALARS scalars double \n')
            # fid.write('LOOKUP_TABLE tableScalar \n')
            # for i in range(len(correctScalars)):
            #     fid.write(correctScalars[i])
            # fid.write('VECTORS vectors double\n')
            # for i in range(len(correctVectors)):
            #     fid.write(correctVectors[i])
            
    print('\nA new file has been created by the name of', vtkFileName, 'in the same directory as this code')
    
main()   