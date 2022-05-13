def compose_map(fun1, fun2, L):
    """
    Returns a new list r where each element in r is fun2(fun1(i)) for the
    corresponding element i in L
    :param fun1: function
    :param fun2: function
    :param L: list
    :return: list
    """
    # listAfterFun1 = [fun1(n) for n in L]    
    # listAfterFun2 = [fun2(i) for i in listAfterFun1]
    listAfterFun = [fun2(fun1(n)) for n in L]
    return(listAfterFun)


def triple_map(fun, L):
    """
    Returns a new list r where each element in r is fun(fun((fun(i))) for the
    corresponding element i in L
    :param fun: function
    :param L: list
    :return: list
    """
    # Fill in
    endList = [fun(fun(fun(i))) for i in L]
    
    return(endList)


def compose(fun1, fun2):
    # Fill in
    """
    Returns a new function f. f should take a single input i, and return
    fun1(fun2(i))
    :param fun1: function
    :param fun2: function
    :return: function
    """
    def ret_fun(i):
        doubleFunList = fun1(fun2(i))
        return(doubleFunList)
    return ret_fun


def repeater(fun, num_repeats):
    """
    Returns a new function f. f should take a single input i, and return
    fun applied to i num_repeats times. In other words, if num_repeats is 1, f
    should return fun(i). If num_repeats is 2, f should return fun(fun(i)). If
    num_repeats is 0, f should return i.
    :param fun: function
    :param num_repeats: int
    :return: function
    """
    def ret_fun(x):
        
        if num_repeats == 0:
            finalOutput = x

        else:
            finalOutput = fun(x)
            
            for i in range(num_repeats - 1):
                finalOutput = fun(finalOutput)
        
        return(finalOutput)
        

    return ret_fun


if __name__ == '__main__':

    def test1(x):
        return x * 2

    def test2(x):
        return x - 3

    data = [2, 5, -10, -7, -7, -3, -1, 9, 8, -6]

    print(compose_map(test1, test2, data))
    print(compose_map(test2, test1, data))
    print(triple_map(test1, data))

    f1 = compose(test1, test2)

    print(f1(4))

    print(list(map(f1, data)))

    f2 = compose(test2, test1)

    print(f2(4))

    print(list(map(f2, data)))

    z = repeater(test1, 0)
    once = repeater(test1, 1)
    twice = repeater(test1, 2)
    thrice = repeater(test1, 3)

    print("repeat 0 times: {}".format(z(5)))
    print("repeat 1 time: {}".format(once(5)))
    print("repeat 2 times: {}".format(twice(5)))
    print("repeat 3 times: {}".format(thrice(5)))