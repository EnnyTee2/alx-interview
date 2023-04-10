#!/usr/bin/python3
""" Prime Game  and Winner Check"""


def isPrime(num):
    for i in range(2, (num//2) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Gets the winner of the Prime Game
    Args:
        x (int): number of rounds
        nums (int): array of n
    Return: name of the winning player
            None if no winner
        n and x are assumed to be <= 10000
    """
    if x < 1 or not nums:
        return None
    Ben = 0
    Maria = 0
    count = 0
    while count < len(nums):
        set_prime = [z for z in range(1, nums[count]+1) if isPrime(z)]
        prime_count = len(set_prime)
        if prime_count % 2 == 0:
            Ben += 1
        else:
            Maria += 1
        count += 1

    if Ben > Maria:
        return 'Ben'
    elif Maria > Ben:
        return 'Maria'
    return None
