def histogram(data, n, b, h):
    # data is a list
    # n is an integer
    # b and h are floats
    
    # Write your code here
    #Here we check if n is positve
    if n < 0:
        print("Please use a positive value for n.")
        pass
    
    #Here in this If statement we error check and 
    #correct the necessary values inside the data list, 
    #as well as change b and h as necessary
    if b < 0: 
        if abs(b) > h:
            h = abs(b)
        b = 0
        
        for i in range(len(data)):
            if data[i] < 0:
                data[i] = abs(data[i])
    
    #Here we create a list with only the values inside the bound interval we've chosen
    dataCopy = []
    for i in range(len(data)):
        if b < data[i] < h:
            dataCopy.append(data[i])
    
    #Now we set up the histogram length, the bin width and the loop to change the values of the histogram accordingly
    hist = [0] * n
    w = (h-b)/n
    
    for i in range(len(hist)):
        for j in range(len(dataCopy)):
            if (b + i * w) <= dataCopy[j] < (b + (i+1) * w):
                
                hist[i] += 1
    
    # return the variable storing the histogram
    # Output should be a list
    return(hist)

def birthdaycake(name_to_day, name_to_month, name_to_year):
    #name_to_day, name_to_month and name_to_year are dictionaries
    import math as m
    # Write your code here
    
    name_to_all = {}
    
    for i in name_to_day:
        name = i
        day = name_to_day[i]
        year = name_to_year[name]
        
        month = name_to_month[name]
        if month == 10 or month == 11 or month == 12:
            year += 5
        
        monthUsedOnEq = month
        yearUsedOnEq = year
        if month <=2:
            yearUsedOnEq -= 1
            monthUsedOnEq += 12
        
        h = (day + m.floor((13 * (monthUsedOnEq + 1)) / 5) + yearUsedOnEq + m.floor(yearUsedOnEq / 4) - m.floor(yearUsedOnEq / 100) + m.floor(yearUsedOnEq / 400)) % 7

        if h == 0:
            weekday = 'Saturday'
        elif h == 1:
            weekday = 'Sunday'
        elif h == 2:
            weekday = 'Monday'
        elif h == 3:
            weekday = 'Tuesday'
        elif h == 4:
            weekday = 'Wednesday'
        elif h == 5:
            weekday = 'Thursday'
        elif h == 6:
            weekday = 'Friday'
        
        dateTuple = ((month, day, year), weekday)
        
        name_to_all.update({name:dateTuple})
        
    # return the variable storing name_to_all
    # Output should be a dictionary
    return(name_to_all)
