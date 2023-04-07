#!/usr/bin/python3
"""
Define isWineer function, a solution to the Prime Game problem
"""


def primes(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None

'''#!/usr/bin/python3
""" Prime Game  and Winner Check"""


def isPrime(num):
    """ checks if a number is prime """
    if num == 1 or num == 0:
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
    for number in nums:
        set_prime = [z for z in range(1, number+1) if isPrime(z)]
        prime_count = len(set_prime)
        if prime_count % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Ben > Maria:
        return 'Ben'
    elif Maria > Ben:
        return 'Maria'
    return None
'''
