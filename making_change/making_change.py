#!/usr/bin/python

import sys


def making_change(amount, denominations):
    if (amount <= 1):
        return 1
    elif(amount < 5):
        return 1
    elif(amount == 5):
        return 2
    elif(amount == 10):
        return 4
    elif(amount < 25):
        return making_change(amount - denominations[0], denominations) + making_change(amount - denominations[1], denominations) + making_change(amount - denominations[2], denominations)
    elif(amount < 50):
        return making_change(amount - denominations[0], denominations) + making_change(amount - denominations[1], denominations) + making_change(amount - denominations[2], denominations) + making_change(amount - denominations[3], denominations)
    elif(amount >= 50):
        return making_change(amount - denominations[0], denominations) + making_change(amount - denominations[1], denominations) + making_change(amount - denominations[2], denominations) + making_change(amount - denominations[3], denominations) + making_change(amount - denominations[4], denominations)


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
