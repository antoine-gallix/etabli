"""tools for measuring time
"""


def timer(f):
    '''
    decorator to print execution time of a function
    :param f:
    '''

    def timedFunction(*args, **kwargs):
        t0 = time()
        out = f(*args, **kwargs)
        t1 = time()
        print("timer :", f.__name__, t1 - t0)
        return out

    return timedFunction
