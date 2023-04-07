#!/usr/bin/python3
''' Prime Number '''


def isPrime(num):
    """ checks if a number is prime """
    status = 1
    if num == 1:
        return False
    index = 0
    prime_fact = [2,3,4,5,6,7,8,9]
    while index < len(prime_fact):
        if num == prime_fact[index]:
            pass
        else:
            status = num % prime_fact[index]
        if status == 0:
            return False
        index += 1
    return True
