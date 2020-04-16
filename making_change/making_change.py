#!/usr/bin/python

import sys


def making_change(amount, denominations, cache=None):
    if cache is None:
        cache = [None] * (amount + 1)
    if(amount == 0):
        cache[amount] = 1
    if(amount == 5):
        cache[amount] = 2
    if(amount == 10):
        cache[amount] = 4
    else:
        for coin in denominations:
            cache[amount] = making_change(amount - coin, denominations)
            return cache

    return cache


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
