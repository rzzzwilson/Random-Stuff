#!/usr/bin/env python3

import time

def find_factors(num):
    """Find factors of a given number 'num'.
    Returns a list containing the factors.
    """

    # prepare the result list
    result = []

    # check for factors of 2
    while not (num % 2):
        result.append(2)
        num = num // 2

    # check for other odd factors, starting at 3
    factor = 3
    while factor <= num:
        while not (num % factor):
            result.append(factor)
            num = num // factor
        factor += 2

    return result

while True:
    # get number to find factors for
    try:
        number = int(input('Enter number: '))
    except ValueError:
        print('Sorry, only positive integers!')
        continue

    # ensure value > 0
    if number < 1:
        print('Sorry, only positive integers!')
        continue

    # get the factors & report
    start = time.time()
    factors = find_factors(number)
    delta = time.time() - start
    print(f'Time taken to execute is: {delta:10.5}s')

    if factors:
        print(f"Factors: {factors}")
    else:
        print('No factors found')
    print()
