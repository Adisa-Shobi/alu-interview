#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n, result=0):
    ''' Returns the minimum number of operations to reach n characters
    '''
    if n <= 1:
        return (0)
    elif n <= 3:
        return (n)
    hcf = get_hcf(n)
    return minOperations(hcf) + (n // hcf)


def get_hcf(num: int) -> int:
    '''Returns the highest common factor of num
    '''
    for i in range(num // 2, 0, -1):
        if num % i == 0:
            return (i)
