#!/usr/bin/python

import sys


# needs to get cached properly
def making_change(amount, denominations):
    if amount < 0:
        return 0
    if amount == 0:
        return 1
    else:
        return sum(making_change(amount - denominations[i], denominations[i:]) for i in range(len(denominations)))


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
