def stencil(data, f, width):
    """
    perform a stencil using the filter f with width w on list data
    output the resulting list
    note that if len(data) = k, len(output) = k - width + 1
    f will accept as input a list of size width and return a single number
    :param data: list
    :param f: function
    :param width: int
    :return: list
    """
    lengthListOutput = len(data) - width + 1
    
    stencilFunctionList = []
    
    for i in range(0, lengthListOutput):
        iterationList = []
        
        for j in range(width):
            currentIndex = i + j
            
            iterationList.append(data[currentIndex])
            
            
        stencilFunctionList.append(f(iterationList))
            
    return(stencilFunctionList)


def create_box(box):
    """
    create a box filter from the input list "box"
    this filter should accept a list of length len(box) and return a simple
    convolution of it.
    the meaning of this box filter is as follows:
    for each element the input list L, multiply L[i] by box[i]
    sum the results of all of these multiplications
    return the sum
    So for a box of length 3, box_filter(L) should return:
      (box[0] * L[0] + box[1] * L[1] + box[2] * L[2])
    The function create_box returns the box filter itself, as well as the length
    of the filter
    :param box: list
    :return: function, int
    """

    # Fill in
    def box_filter(L):
        boxValue = 0
        for i in range(len(box)):
            boxValue += box[i] * L[i]     
        
        return(boxValue)

    return box_filter, len(box)


if __name__ == '__main__':

    def mov_avg(L):
        if len(L) != 3:
            raise ValueError(f'Expected list of length 3 for mov_avg but got list of length {len(L)}.')
        return float(sum(L)) / 3

    def sum_sq(L):
        if len(L) != 5:
            raise ValueError(f'Expected list of length 5 for sum_sq but got list of length {len(L)}.')
        return sum([i**2 for i in L])
    
    data = [2, 5, -10, -7, -7, -3, -1, 9, 8, -6]

    print(stencil(data, mov_avg, 3))
    print(stencil(data, sum_sq, 5))

    # note that this creates a moving average!
    box_f1, width1 = create_box([1.0 / 3, 1.0 / 3, 1.0 / 3])
    print(stencil(data, box_f1, width1))

    box_f2, width2 = create_box([-0.5, 0, 0, 0.5])
    print(stencil(data, box_f2, width2))