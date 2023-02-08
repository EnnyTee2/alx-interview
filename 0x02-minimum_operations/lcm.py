#!/usr/bin/python3
''' LCM generator '''


from typing import List
global factors
factors = (2, 3, 5, 7)


def lcm_gen(num):
    '''Generates the LCMs for a given number'''
    for factor in factors:
        if (num % factor) == 0:
            yield factor
            yield from lcm_gen(num // factor)  # recursive part of generator
            break
        else:
            if (factor == 7) and (num != 1):
                yield num


def lcm(num) -> List[int]:
    '''Combines the yields from lcm generator'''
    if num <= 1:
        return 0
    return list(lcm_gen(num))  # combine the yields from lcm generator
