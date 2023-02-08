#!/usr/bin/python3
'''ALX Minimum Operatiions Interview Question'''


lcm = __import__('lcm').lcm


def minOperations(n):
    '''Returns the fewest number of operations'''
    return sum(lcm(n))
