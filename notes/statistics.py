'Awesome statistical analysis project'

from __future__ import division

def average(seq):
    '''Compute the arithmetic mean

            >>> average([10, 20, 60])
            30.0
            >>> average([10, 20, 61])
            30.333333333333332

    '''
    return sum(seq) / len(seq)

data = [10, 50, 15, 60, 25, 100, 28, 150, 12]

def median(data):
    '''Show the middlemost element of an array of data

            >>> median([10, 50, 15, 60, 25, 100, 28, 150, 12])
            28
    '''
    midpoint = len(data) // 2
    return sorted(data)[midpoint]

if __name__ == '__main__':
    import doctest

    print doctest.testmod()
