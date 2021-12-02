from typing import List


def maxProfit(prices: List[int]) -> int:
    # buy = prices[0]
    # # sell = prices[0]
    # max_profit = 0
    # for i in range(1, len(prices)):
    #     buy = min_buy(buy, prices[i])
    #     if prices[i] - buy > max_profit:
    #         max_profit = prices[i] - buy
    #     # sell =
    #     # buy = min_buy(buy, prices[i])
    # return max_profit

    min_buy = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        if min_buy > prices[i]:
            min_buy = prices[i]
        else:
            max_profit += prices[i] - min_buy
            min_buy = prices[i]
    print(max_profit)
    return max_profit

    '''
    optimal solution
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i-1] < prices[i]:
            max_profit += prices[i] - prices[i-1]
    return max_profit
    '''


maxProfit([7, 1, 5, 3, 6, 4])
maxProfit([1, 2, 3, 4, 5])
maxProfit([7, 6, 4, 3, 1])

# [7, 1, 5, 3, 6, 4]
# [7]
# i = 0
#    buy = prices[0] = 7
#     sell = prices[0] = 7
#     max_profit = 0
# i = 1
# [7, 1]
#    buy
#        if price[i] < buy:
#             buy = price[i]
#         else:
#             do_nothing
#         if 1 < 7: #true
#             buy = 1
#     sell
#        if prices[i] - buy > max_profit:
#             sell = prices[i] - buy
#             max_profit += sell
#             buy = price[i]  # potentially buy at price[i]
#         else:
#             do_not_sell
#         if 1 - 7 > 0 #false
#         else:
#             sell = 7, max_profit = 0

# i = 2
# [7, 1, 5]
#    buy
#        if price[i] < buy:
#             buy = price[i]
#         else:
#             do_nothing
#         if 5 < 1 #false
#         else:
#             buy = 1
#     sell
#        if prices[i] - buy > max_profit:
#             sell = prices[i] - buy
#             max_profit += sell
#             buy = price[i]
#         else:
#             do_not_sell
#         if 5 - 1 > 0 #true
#            sell = 5 - 1 = 4
#             max_profit = 4
#             buy = 5

# i = 3
# [7, 1, 5, 3]
#    buy
#        if price[i] < buy:
#             buy = price[i]
#         else:
#             do_nothing
#         if 3 < 5 #true
#            buy = 3
#     sell
#        if prices[i] - buy > max_profit:
#             sell = prices[i] - buy
#             max_profit += sell
#         else:
#             do_not_sell
#         if 3 - 3 > 4 #false
#         else:
#             max_profit = 4

# i = 4
# [7, 1, 5, 3, 6]
#    buy
#        if price[i] < buy:
#             buy = price[i]
#         else:
#             do_nothing
#         if 6 < 3 #false
#         else:
#             buy = 3
#     sell
#        if prices[i] - buy > max_profit:
#             sell = prices[i] - buy
#             max_profit += sell
#         else:
#             do_not_sell
#         if 6 - 3 > 4 #false
#         else:
#             max_profit = 4 # <== wrong here, at this pount, max_profit =  4 + 3 = 7

# [7, 1, 5, 3, 6, 4]
# [7]
# i = 0
#    buy = prices[0] = 7
#     # sell = prices[0] = 7
#     max_profit = 0

# [7, 1]
# i = 1
#    buy: choose between selling what bought or shouldn't have bought first one and buy now at prices[i]
#        buy = min(prices[i], buy)
#         buy = min(1, 7) = 1
#     max_profit: choose between selling the stock or do nothing
#         max_profit = max_profit + max(0, prices[i] - buy)
#         max_profit = 0 + max(0, 0) = 0
# [7, 1, 5]
# i = 2
#    buy:
#         buy = min(prices[i], buy)
#         buy = min(5, 1) = 1
#     max_profit:
#         max_profit = max_profit + max(0, prices[i] - buy)
#         max_profit = 0 + max(0, 4) = 4
# [7, 1, 5, 3]
# i = 2
#    buy
#        buy = min(prices[i], buy)
#         buy = min(3, 1) = 1 <= = wrong here, at this point, buy = 3
#     max_profit:
#         max_profit = max_profit + max(0, prices[i] - buy)
#         max_profit = 4 + max(0, 2) = 6 <= = wrong here, at this point, max_profit = 4

# [7, 1, 5, 3, 6, 4]
# [7]
# i = 0
#     buy = prices[0] = 7
#     sell = prices[0] = 0
#     max_profit = 0

# [7, 1]
# i = 1
#    buy
#         buy = min(max_profit + buy, prices[i])
#         buy = min(0 + buy, prices[i])
#         buy = min(7, 1) = 1
#     sell
#        sell = 1 # = max(sell, price[i])
#     max_profit
#        max_profit = 0 # = max_profit + max(0, buy - sell) = 0 + 1 - 1
# [7, 1, 5]
# i = 2
#    buy
#         buy = min(max_profit + buy, prices[i])
#         buy = min(0 + 1, 5)
#         buy = 1
#     sell
#        sell = 5 # = max(sell, price[i])
#     max_profit
#        max_profit = 0 # = max_profit + max(0, buy - sell) = 0 + max(0, 4) = 4
# [7, 1, 5, 3]
# i = 3
#     buy
#         buy = min(max_profit + buy, prices[i])
#         buy = min(4 + 1, 3)
#         buy = 3
#     sell
#         sell = 5 # = max(sell, price[i])
#     max_profit
#        max_profit = 0 # = max_profit + max(0, sell - buy) = 4 + max(0, -2) = 4

# [7, 1, 5, 3, 6]
# i = 4
#    buy
#         buy = min(max_profit + buy, prices[i])
#         buy = min(4+1, 3)
#         buy = 3
#     sell
#        sell = 6 # = max(sell, price[i])
#     max_profit
#        max_profit = 0 # = max_profit + max(0, buy - sell) = 4 + max(0,) = 4

# [7, 1, 5, 3, 6, 4]
# [7]
# i = 0
#     buy:
#         either buy at price[i]
#             buy = 7
#         or not buy
#             buy = 0
#     sell:
#         sell at prices[i] if max_profit[i] > max_profit[i-1]
#         else no sell
#     max_profit:
#         max_profit += sell - buy
# [7, 1]
# i = 1
#     buy:
#         if at i-1 not buy, 2 options
#             not buy
#                 buy = 0
#             buy at price[i]
#         if at i-1 buy, whether to buy?

# [7, 1, 5, 3, 6, 4]
#    if min > prices[i]:
#         min = prices[i]
#     else:
#         max_profit += prices[i] - min
#         min = prices[i]

#     if 6 > 4:  # true
#         min = 4
#     max_profit = 7

# [7, 1, 5, 3, 6]
# i = 4
#    if min > prices[i]:
#         min = prices[i]
#     else:
#         max_profit += prices[i] - min
#         min = prices[i]

#     if 3 > 6:  # false
#     else:
#         max_profit = 4 + 6 - 3 = 7
#         min = 6

# [7, 1, 5, 3]
# i = 3
#    if min > prices[i]:
#         min = prices[i]
#     else:
#         max_profit += prices[i] - min
#         min = prices[i]

#     if 5 > 3:  # true
#         min = 3
#     max_profit = 4
# [7, 1, 5]
# i = 2
#    if min > prices[i]:
#         min = prices[i]
#     else:
#         max_profit += prices[i] - min
#         min = prices[i]

#     if 1 > 5:  # false
#     else:
#         max_profit = 0 + 5 - 1 = 4
#         min = 5
# [7, 1]
# i = 1
#    if min > prices[i]:
#         min = prices[i]
#     else:
#         max_profit += prices[i] - min

#     if 7 > 1:  # true
#         min = 1
#     max_profit = 0
# [7]
# i = 0
#    min = 7
#     max_profit = 0
