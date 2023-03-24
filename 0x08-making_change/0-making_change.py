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
    coins = sorted(coins, reverse=True)
    maxi = coins[1]
    x = 0
    coins.pop(0)
    rem = total % maxi
    if rem == 0:
        return total / maxi
    quot = total // maxi
    while x < len(coins):
        remc = rem % coins[x]
        if remc == 0:
            return quot + (rem // coins[x])
        if x == 0:
            return -1
        quotc = remc // coins[x]
        rem = remc
        quot += quotc
        x += 1
    return quot
