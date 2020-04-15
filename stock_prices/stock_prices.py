#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # sets initial min value
    current_min_price = [prices[0], 0]
    max_profit = 0
    if(len(prices) <= 1):
        return None

    for i in range(len(prices)):

        print(
            f"current min: {current_min_price[0]}\ncurrent price: {prices[i]}\ncurrent max profit: {max_profit}")

        if(prices[i] - current_min_price[0] > max_profit and i > current_min_price[1]):
            print(prices)
            max_profit = prices[i] - current_min_price[0]

        if(prices[i] < current_min_price[0]):
            current_min_price[0] = prices[i]
            current_min_price[1] = i

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
