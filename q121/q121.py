from typing import List


def maxProfit(prices: List[int]) -> int:
    # sorted_prices = prices.copy()
    # sorted_prices.sort()
    # max_profit = 0
    # i = 0
    # while max_profit == 0 and i < len(sorted_prices):
    #     for j in range(len(sorted_prices)-1, i, -1):
    #         if prices.index(sorted_prices[j]) > prices.index(sorted_prices[i]):
    #             max_profit = sorted_prices[j] - sorted_prices[i]
    #             break
    #     i += 1

    # sorted_prices = []
    # for i, j in enumerate(prices):
    #     sorted_prices.append((j, i))

    # sorted_prices.sort(key=lambda x: (x)[0])

    # i = 0
    # is_break = False
    # while i < len(sorted_prices) and is_break == False:
    #     for j in range(len(sorted_prices)-1, i, -1):
    #         if sorted_prices[i][1] < sorted_prices[j][1]:
    #             profit = sorted_prices[j][0] - sorted_prices[i][0]
    #             if profit > max_profit:
    #                 max_profit = profit
    #                 is_break = True
    #     i += 1

    # cash, hold = 0, -prices[0]
    # days = len(prices)
    # for i in range(1, days):
    #     cash = max(cash, hold+prices[i])
    #     hold = max(hold, cash-prices[i])
    # return cash

    # break_loop = False
    # first_max, first_min = max(prices), min(prices)
    # max_index = prices.index(first_max)
    # min_index = prices.index(first_min)
    # max_profit = 0
    # while not break_loop and len(prices) > 1:
    #     if max_index > min_index:
    #         max_profit = first_max - first_min
    #         break_loop = True
    #     elif len(prices) > 3:
    #         # if first_max in prices:
    #         prices.pop(max_index)
    #         # if first_min in prices:
    #         prices.pop(min_index-1)
    #         next_max = max(prices)
    #         next_min = min(prices)
    #         next_max_index = prices.index(next_max)+2
    #         next_min_index = prices.index(next_min)+2
    #         if max_index > next_min_index:
    #             max_profit = max(max_profit, first_max - next_min)
    #             break_loop = True
    #         if next_max_index > min_index:
    #             max_profit = max(max_profit, next_max - first_min)
    #             break_loop = True

    #         first_max = next_max
    #         first_min = next_min
    #         max_index = next_max_index-2
    #         min_index = next_min_index-2
    #     else:
    #         break_loop = True

    # return max_profit

    # sorted_prices = []
    # for index, value in enumerate(prices):
    #     sorted_prices.append((value, index))
    # len_prices = len(prices)
    # number_of_digit_len_prices = len(str(len_prices))
    # denominator = 10**number_of_digit_len_prices
    # sorted_prices.sort(
    #     key=lambda x: x[0]+x[1]/denominator
    # )

    # break_loop = False
    # first_max, first_min = sorted_prices[-1][0], sorted_prices[0][0]
    # max_index, min_index = sorted_prices[-1][1], sorted_prices[0][1]
    # max_profit = 0
    # while not break_loop and len_prices > 1:
    #     if max_index > min_index:
    #         max_profit = first_max - first_min
    #         break_loop = True
    #     elif len_prices > 2:
    #         # if first_max in prices:
    #         sorted_prices.pop(0)
    #         # if first_min in prices:
    #         sorted_prices.pop(-1)
    #         len_prices -= 2
    #         next_max, next_min = sorted_prices[-1][0], sorted_prices[0][0]
    #         next_max_index = sorted_prices[-1][1]
    #         next_min_index = sorted_prices[0][1]
    #         if max_index > next_min_index:
    #             max_profit = max(max_profit, first_max - next_min)
    #             break_loop = True
    #         if next_max_index > min_index:
    #             max_profit = max(max_profit, next_max - first_min)
    #             break_loop = True

    #         first_max = next_max
    #         first_min = next_min
    #         max_index = next_max_index
    #         min_index = next_min_index
    #     else:
    #         break_loop = True

    # return max_profit

    # max_price = -1
    # min_price = prices[0]
    # for i in range(1, len(prices)):
    #     if max_price > prices[i]:
    #         min_price = min_price  # do nothing
    #     else:
    #         min_price = min(min_price, prices[i])
    #     max_price = max(max_price, prices[i])

    # if max_price > min_price:
    #     return max_price - min_price
    # else:
    #     return 0

    # sell_price = prices[0]
    buy_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] - buy_price > max_profit:
            # sell_price = prices[i]
            max_profit = prices[i] - buy_price

        if buy_price > prices[i]:
            buy_price = prices[i]

    print(max_profit)
    return max_profit

    ''' Final Solution
    buy_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - buy_price)
        buy_price = min(buy_price, prices[i])

    return max_profit
    '''


maxProfit([7, 1, 5, 3, 6, 4])
maxProfit([7, 6, 4, 3, 1])
maxProfit([2, 1, 2, 0, 1])
maxProfit([3, 2, 6, 5, 0, 3])
maxProfit([2, 4, 1])
maxProfit([4, 7, 1, 2])
maxProfit([1, 2])
maxProfit([2, 1, 2, 1, 0, 1, 2])

################################################################################
# [3, 2, 6, 5, 0, 3]
# i = 0; cash[0] = 0, hold[0] = 3
# i = 1;  cash[1]:
#             - not buying:   a = cash[0] = 0
#             - selling:      b = price[1] - hold[0] = 2 - 3 = -1
#             - max:          max(a, b) = 0
#         hold[1]:
#             - not selling:  a=hold[0] = 3
#             - buying:       b=cash[1] - price[1] = 0 - 2 = -2
#             - max:          max(a,b) = 3
# i = 2;  cash[2]:
#             - not buying:   a=cash[1] = 0
#             - selling:      b=price[2] - hold[1] = 6 - 3 = 3
#             - max:          max(a,b) = 3
#         hold[2]:
#             - not selling:  a=hold[1] = 3
#             - buying:       b=cash[2] - price[2] = 3 - 6 = -3
#             - max:          max(a,b) = 3
# i = 3;  cash[3]:
#             - not buying:   a=cash[2] = 3
#             - selling:      b=price[3] - hold[2] = 5 - 3 = 2
#             - max:          max(a,b) = 3
#         hold[3]:
#             - not selling:  a=hold[2] = 3
#             - buying:       b=cash[3] - price[3] = 3 - 5 = -2
#             - max:          max(a,b) = 3
# i = 4;  cash[4]:
#             - not buying:   a=cash[3] = 3
#             - selling:      b=price[4] - hold[3] = 0 - 3 = -3
#             - max:          max(a,b) = 3
#         hold[4]:
#             - not selling:  a=hold[3] = 3
#             - buying:       b=cash[4] - price[4] = 3 - 0 = 3
#             - max:          max(a,b) = 3
# i = 5;  cash[5]:
#             - not buying:   a=cash[4] = 3
#             - selling:      b=price[5] - hold[4] = 3 - 3 = 0
#             - max:          max(a,b) = 3
#         hold[5]:
#             - not selling:  a=hold[4] = 3
#             - buying:       b=cash[5] - price[5] = 3 - 3 = 0
#             - max:          max(a,b) = 3

# [3, 2, 6, 5, 0, 3]
# i = 0; buy[0] = 3, sell[0] = 0
# i = 1;  buy[1]:
#                 - not buy price[i], best buy is buy[i-1]: a = buy[0] = 3
#                 - not buy at price[i-1], buy at price[i]: b = price[1] = 2
#                 - min(a, b) = 2
#         sell[1]:
#                 - not sell at price[i], best sell is sell[i-1]: a = sell[0] = 0
#                 - sell at price[i]: b = price[1] = 2
#                 - max(a,b) = 2
# i = 2;  buy[2]:
#                 - not buy price[i], best buy is buy[i-1]: a = buy[1] = 2
#                 - not buy at price[i-1], buy at price[i]: b = price[1] = 2
#                 - min(a,b) = 2
#         sell[2]:
#                 - not sell at price[i], best sell is sell[i-1]: a = sell[1] = 2
#                 - sell at price[i]: b = price[2] = 6
#                 - max(a,b) = 6
# i = 3;  buy[3]:
#                 - not buy price[i], best buy is buy[i-1]: a = buy[2] = 2
#                 - not buy at price[i-1], buy at price[i]: b = price[2] = 6
#                 - min(a,b) = 2
#         sell[3]:
#                 - not sell at price[i], best sell is sell[i-1]: a = sell[2] = 6
#                 - sell at price[i]: b = price[3] = 5
#                 - max(a,b) = 6
# i = 4;  buy[4]:
#                 - not buy price[i], best buy is buy[i-1]: a = buy[3] = 2
#                 - not buy at price[i-1], buy at price[i]: b = price[4] = 0
#                 - min(a,b) = 0 <== wrong
#         sell[4]:
#                 - not sell at price[i], best sell is sell[i-1]: a = sell[3] = 6
#                 - sell at price[i]: b = price[3] = 5
#                 - max(a,b) = 6

# [3, 2, 6, 5, 0, 3]
# i = 0:
#     - if buy at price[i]: buy = price[0] = 3
#     - if not buy at price[i]: buy = 0

#     - if not sell at price[i]: sell = 0
#     - Nothing to sell yet
# i = 1
#     - if buy in i-1, no buy: buy = buy[0] = 3
#     - if not buy in i-1, buy at price[i] buy = price[1] = 2
#     - if not buy in i-1, continue not buy: buy = 0

#     - if not sell at price[i]: sell = 0
#     - if sell at price[i]: sell = 2
# i = 2
#     - if buy in i-1, no buy: buy = buy[1] = 3
#     - if not buy in i-1, buy at price[i] buy = price[1] = 2
#     - if not buy in i-1, continue not buy: buy = 0

#     - if not sell at price[i]: sell = 0
#     - if sell at price[i]: sell = 2


# While break_loop == false:
# [3, 2, 6, 5, 0, 3]:
#     max = 6, min = 2, i_max = 2, i_min = 1
#     if i_max > i_min:
#         # True
#         max_profit = max - min = 4
#         break_loop = True
#     else:
#         pop element at i_max


# While break_loop == false:
# [7, 1, 5, 3, 6, 4]
#     max = 7, min = 1, i_max = 0, i_min = 1
#     if i_max > i_min:
#         # False
#         max_profit = max - min
#         break_loop = True
#     else:
#         pop element at i_max
# [1, 5, 3, 6, 4]
#   max = 6, min = 1, i_max = 3, i_min = 0
#    if i_max > i_min:
#         # False
#         max_profit = max - min
#         break_loop = True
#     else:
#         pop element at i_max

# moving windows:
# [7, 1, 5, 3, 6, 4]
# max = 0
# left    right   price_left  price_right max(max, price_right - price_left)
# 0       5       7           4           0
# 1       5       1           4           3

# [7, 1, 5, 3, 6, 4]
# i = 0:
#     max = -1
#     min = price[0] = 7
# i = 1:
#     min
#        if max > price[i]:
#             min = min = > if (-1 > 1)  # False
#         else:
#             min = min(min,price[i]) = min(7,1) = 1 # True
#     max = max(max, price[i]) = 1

# i = 2:
#     min
#        if max > price[i]:
#             min = min = > if (1 > 5) # False
#         else:
#             min = min(min,price[i]) = min(1,5) = 1 # True
#     max = max(max, price[i]) = 5
# i = 3:
#     min
#        if max > price[i]:
#             min = min = > if (5 > 3): min = 1# True
#         else:
#             min = min(min,price[i]) # False
#     max = max(max, price[i]) = 5
# i = 4:
#     min
#        if max > price[i]:
#             min = min = > if (5 > 6)# False
#         else:
#             min = min(min,price[i]) = min(1,6) = 1 # True
#     max = max(max, price[i]) = 6
# i = 5:
#     min
#        if max > price[i]:
#             min = min = > if (6 > 4): min = 1# True
#         else:
#             min = min(min,price[i]) # False
#     max = max(max, price[i]) = 6

# [2, 1, 2, 1, 0, 1, 2]
# [2]
# i = 0
#     sell_price[0] = prices[i] = 2
#     buy_price[0] = prices[i] = 2
#     max_profit = 0
# [2, 1]
# i = 1
#     sell_price:
#         if price[i] - buy_price > max_profit:
#             sell_price = price[i]
#             max_profit = price[i] - buy_price
#         else:
#             do_nothing
#         if 1 - 2 > 0:  # false
#         else:
#             sell_price = 2
#     buy_price:
#         if buy_price > price[i]:
#             buy_price = prices[i]
#         else:
#             do_nothing
#         if 2 > 1:
#             buy_price = 1
#     max_profit = 0
# [2, 1, 2]
# i = 3
#    sell_price:
#         if price[i] - buy_price > max_profit:
#             sell_price = price[i]
#             max_profit = price[i] - buy_price
#         else:
#             do_nothing
#         if 2 - 1 > 0:  # true
#             sell_price = 2
#             max_profit = 2 - 1 = 1

#     buy_price:
#         if buy_price > price[i]:
#             buy_price = prices[i]
#         else:
#             do_nothing
#         if 1 > 2: #false
#         else:
#             buy_price = 1

# [2, 1, 2, 1]
# i = 4
#    sell_price:
#         if price[i] - buy_price > max_profit:
#             sell_price = price[i]
#             max_profit = price[i] - buy_price
#         else:
#             do_nothing
#         if 1 - 1 > 1: # false
#         else:
#             sell_price = 2

#     buy_price:
#         if buy_price > price[i]:
#             buy_price = prices[i]
#         else:
#             do_nothing
#         if 1 > 1: #false
#         else:
#             buy_price = 1
#     max_profit = 1
# [2, 1, 2, 1, 0]
# i = 4
#    sell_price:
#         if price[i] - buy_price > max_profit:
#             sell_price = price[i]
#             max_profit = price[i] - buy_price
#         else:
#             do_nothing
#         if 0 - 1 > 1: # false
#         else:
#             sell_price = 2

#     buy_price:
#         if buy_price > price[i]:
#             buy_price = prices[i]
#         else:
#             do_nothing
#         if 1 > 0: #true
#             buy_price = 0
#     max_profit = 1
# [2, 1, 2, 1, 0, 1]
# i = 5
#    sell_price:
#         if price[i] - buy_price > max_profit:
#             sell_price = price[i]
#             max_profit = price[i] - buy_price
#         else:
#             do_nothing
#         if 1 - 0 > 1: # false
#         else:
#             sell_price = 2

#     buy_price:
#         if buy_price > price[i]:
#             buy_price = prices[i]
#         else:
#             do_nothing
#         if 0 > 1: #false
#         else:
#             buy_price = 0
#     max_profit = 1
# [2, 1, 2, 1, 0, 1, 2]
# i = 6
#    sell_price:
#         if price[i] - buy_price > max_profit:
#             sell_price = price[i]
#             max_profit = price[i] - buy_price
#         else:
#             do_nothing
#         if 2 - 0 > 1: # true
#             sell_price = 2
#             max_profit = 2 - 0 = 2

#     buy_price:
#         if buy_price > price[i]:
#             buy_price = prices[i]
#         else:
#             do_nothing
#         if 0 > 2: #false
#         else:
#             buy_price = 0
