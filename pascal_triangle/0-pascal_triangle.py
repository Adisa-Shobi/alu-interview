#!/usr/bin/python3
'''
File defines pascal_triangle function
'''


def pascal_triangle(n):
    '''
    Function returns a list of lists of integers
    representing the pascals triangle
    '''
    triangle = []
    if n <= 0:
        return(triangle)
    for line in range(1, n + 1):
        sub_triangle = []
        prev = 1
        for index in range(1, line + 1):
            sub_triangle.append(int(prev))
            prev = prev * (line - index)/index
        triangle.append(sub_triangle)
    return(triangle)
