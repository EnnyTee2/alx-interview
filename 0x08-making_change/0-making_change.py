#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any
        number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    """
    if total <= 0:
        return 0
    coins.sort()
    max = coins[-1]
    coins.pop()
    rem = total % maxi
    if rem == 0:
        return total / maxi
    quot = total // maxi
    for x in range(len(coins), 0, -1):
        remc = rem % coins[x]
	if remc == 0:
            return quot + (rem // coins[x])
	if x == 0:
            return -1
	quotc = rem // coins[x]
	rem = remc
	quot += quotc
    return quot
        
