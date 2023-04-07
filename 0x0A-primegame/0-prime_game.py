#!/usr/bin/python3
""" Prime Game """


def isPrime(num):
    """ checks if a number is prime """
    if num == 1:
        return False
    status = 1
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
    Gets the winner of the Prime Game
    Args:
        x (int): number of rounds
        nums (int): array of n
    Return: name of the winning player
            None if no winner
        n and x are assumed to be <= 10000
    """
    if x is None or nums is None or x < 1 or nums == []:
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


''' #!/usr/bin/python3
"""This function contains the isWinner function"""


def isWinner(x, nums):
    """This function Determines the winner of a prime game session
    with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
'''
