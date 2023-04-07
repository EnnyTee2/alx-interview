#!/usr/bin/python3
""" Prime Game """

                
def isWinner(x, nums):
    """
        x: number of rounds
        nums: array of n
        Returns: name of the winning player
        n and x are assumed to be <= 10000
    """

    isPrime = __import__('isPrime').isPrime
    Ben = 0
    Maria = 0
    for number in nums:
        set_prime = [z for z in range(1, number+1) if isPrime(z)]
        count = 0
        M,B = (0,1)
        prime_count = len(set_prime)
        while count < prime_count:
            if count % 2 == 0:
                M,B = (1,0)
            else:
                M,B = (0,1) 
            count += 1
        Ben += B
        Maria += M

    if Ben == Maria:
        return None
    elif Ben > Maria:
        return Ben
    else:
        return Maria      
