#!/usr/bin/python3
""" Prime Game """


def isPrime(num):
    """ checks if a number is prime """

    status = 1
    if num == 1:
        return False
    index = 0
    prime_fact = [2, 3, 4, 5, 6, 7, 8, 9]
    while index < len(prime_fact):
        if num == prime_fact[index]:
            pass
        else:
            status = num % prime_fact[index]
        if status == 0:
            return False
        index += 1
    return True


def isWinner(x, nums):
    """
        x: number of rounds
        nums: array of n
        Returns: name of the winning player
        n and x are assumed to be <= 10000
    """

    if x is None or nums is None or x == 0 or nums == []:
        return None
    Ben = 0
    Maria = 0
    for number in nums:
        set_prime = [z for z in range(1, number+1) if isPrime(z)]
        count = 0
        M, B = (0, 1)
        prime_count = len(set_prime)
        while count < prime_count:
            if count % 2 == 0:
                M, B = (1, 0)
            else:
                M, B = (0, 1)
            count += 1
            Ben += B
            Maria += M

    if Ben == Maria:
        return None
    elif Ben > Maria:
        return 'Ben'
    else:
        return 'Maria'
