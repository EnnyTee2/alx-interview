#!/usr/bin/python3
""" Prime Game  and Winner Check"""


def isPrime(num):
    """ checks if a number is prime """
    if num < 2:
        return False
    index = 0
    status = 1
    prime_fact = [2, 3, 5, 7]
    while index < len(prime_fact):
        if prime_fact[index] == num:
            pass
        else:
            status = num % prime_fact[index]
        if status == 0:
            return False
        index += 1
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
    print(f'Ben: {Ben} and Maria: {Maria}')
    if Ben > Maria:
        return 'Ben'
    elif Maria > Ben:
        return 'Maria'
    return None
