import sys


def maxProfit(prices, fee) -> int:
    # # Time Limit Exceeded
    # global max_profit
    # max_profit = -sys.maxsize

    # def recurse(choices, profit, i):
    #     global max_profit
    #     if i < len(prices):
    #         for choice in choices:
    #             if abs(choice) == 1:
    #                 next_choices = [0, -choice]
    #                 profit += prices[i]*choice
    #                 if choice == 1:
    #                     profit -= fee
    #             else:
    #                 next_choices = choices
    #             recurse(next_choices, profit, i+1)
    #             profit -= prices[i]*choice
    #             if choice == 1:
    #                 profit += fee

    #     elif i == len(prices):
    #         if profit > max_profit:
    #             max_profit = profit

    # # -1 = buy, 1=sell
    # intial_choices = [0, -1]
    # recurse(intial_choices, 0, 0)
    # return max_profit

    ###
    #  Dynamic Programming
    # cash, hold = 0, -prices[0]
    # days = len(prices)
    # for i in range(1, days):
    #     cash = max(cash, hold+prices[i]-fee)
    #     hold = max(hold, cash-prices[i])
    # return cash

    cur_not_hold = 0
    cur_hold = -float('inf')

    for i in range(0, len(prices)):
        prev_not_hold = cur_not_hold
        prev_hold = cur_hold

        cur_not_hold = max(prev_not_hold, prev_hold + prices[i] - fee)
        cur_hold = max(prev_hold, prev_not_hold - prices[i])

    return cur_not_hold


print(maxProfit([1, 3, 2, 8, 4, 9], 2))
print(maxProfit([1, 3, 7, 5, 10, 3], 3))

# Best explanation https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/189842
