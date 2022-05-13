import numpy as np
import matplotlib.pyplot as plt


def norm_histogram(hist):
    totalBins = sum(hist)
    probabilityHist = []
    for i in hist:
        probabilityHist.append(i / totalBins)
    return(probabilityHist)


def compute_j(histo, width):
    """
    takes histogram of counts, uses norm_histogram to convert to probabilties, it then calculates compute_j for one bin width

    :param histo: list 
    :param width: float
    :return: float
    """
    probabilityHist = norm_histogram(histo)
    probabilitySquareList = []
    for i in probabilityHist:
        probabilitySquareList.append(i ** 2)
    
    probabilitySquareSum = sum(probabilitySquareList)
    
    numberSamples = sum(histo)

    jValue = (2 / ((numberSamples - 1) * width)) - ((numberSamples + 1) / ((numberSamples - 1) * width)) * (probabilitySquareSum)
  
    return(format(jValue, '0.4f'))
  
def sweep_n(data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate compute_j for a full sweep [min_bins to max_bins]
    please make sure max_bins is included in your sweep

    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    stdDev = np.std(data)
    
    jvalues = []
    
    for i in range(min_bins, max_bins + 1):
        histogram = plt.hist(data, i, (minimum, maximum))[0]
        
        numSamples = sum(histogram)
        
        binWidth = (maximum - minimum) / i
        
        jValue = compute_j(histogram, binWidth)
        
        jvalues.append(float(jValue))

    return(jvalues)

def find_min(l):
    """
    Generic function that takes a list of numbers and returns the smallest number in that list and its index in the list.
    It will return the optimal value and the index of the optimal value as a tuple.

    :param l: list
    :return: tuple
    """
    optimalTuple = (min(l), l.index(min(l)))
    
    return(optimalTuple)


if __name__ == '__main__':
    data = np.loadtxt('input.txt')  # reads data from input.txt
    lo = min(data)
    hi = max(data)
    bin_l = 1
    bin_h = 100
    js = sweep_n(data, lo, hi, bin_l, bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bounds of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(find_min(js))
