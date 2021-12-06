from typing import List


def maxProfit(prices: List[int]) -> int:
    # brute force
    # max_profit = 0
    # for i in range(len(prices)):
    #     for j in range(i+1,len(prices)):
    #         if prices[i] < prices[j]:

    cur_hold = -float('inf')
    cur_not_hold = 0
    cur_cooldown = 0

    for i in range(0, len(prices)):
        prev_hold = cur_hold
        prev_not_hold = cur_not_hold
        prev_cooldown = cur_cooldown

        cur_hold = max(prev_hold, prev_cooldown - prices[i])
        cur_not_hold = max(prev_not_hold, prev_hold + prices[i])
        cur_cooldown = max(prev_cooldown, prev_not_hold)

    print(cur_not_hold)
    return cur_not_hold


maxProfit([1, 2, 3, 0, 2])
maxProfit([1])


# [1, 2, 3, 0, 2, 5]
# [1]
#     min_buy = prices[0] = 1
#     max_profit = 0
# [1, 2]
#     min_buy = 2
#         min_buy > prices[i]:
#             if i != i_cool
#                 min_buy = prices[i]
#             else:
#                 ...
#         else:
#             max_profit += prices[i] - min_buy
#             i_cool = i + 1
#             min_buy = prices[i]

#         if 1 > 2 # false
#         else:
#             max_profit = 0 + 2 - 1 = 1
#             i_cool = 2
#             min_buy = 2
#     max_profit = 1
#     i_cool = 2

# [1, 2, 3]
#     min_buy = 3
#         min_buy > prices[i]:
#             if i != i_cool
#                 min_buy = prices[i]
#             else:
#                 ...
#         else:
#             max_profit += prices[i] - min_buy
#             i_cool = i + 1
#             min_buy = prices[i]
#         if 2 > 3 # false
#         else:
#             max_profit = 1 + 3 - 2 = 2
#             i_cool = 3
#             min_buy = 3
#     max_profit = 2
#     i_cool = 3

# [1, 2, 3, 0]
#     min_buy = 3
#         min_buy > prices[i]:
#             if i != i_cool
#                 min_buy = prices[i]
#             else:
#                 ...
#         else:
#             max_profit += prices[i] - min_buy
#             i_cool = i + 1
#             min_buy = prices[i]
#         if 3 > 0 # true
#             if 3 != 3 #false
#     max_profit = 2
#     i_cool = 3
# [1, 2, 3, 0, 2]
#     min_buy = 2
#         min_buy > prices[i]:
#             if i != i_cool
#                 min_buy = prices[i]
#             else:
#                 ...
#         else:
#             max_profit += prices[i] - min_buy
#             i_cool = i + 1
#             min_buy = prices[i]
#         if 3 > 2 # true
#             if 4 != 3 #true
#                 min_buy = 2
#     max_profit = 2 # <== wrong here max_profit = 3
#     i_cool = 3  # <== wrong here i_cool = 2

# [1, 2, 3, 0, 2, 5]
#     max_profit = 5
#     i_cool = 5


# [1, 2, 3, 0, 2, 5]
# [1]
#     # if len(prices) < 2:
#     #     max_profit = max(0, prices[-1] - prices[0]) = 0
#     last_sell = prices[0] = 1
#     min_buy = prices[0] = 1
#     max_profit = 0
# [1, 2]
# #    if len(prices) < 3:
# #         max_profit = max(0, prices[-1] - prices[0]) = 1
# #         if max_profit > 0  # transaction occurs
# #            last_sell = 2
# #            min_buy = 1
# #         else:
# #             min_buy = 1
# #             last_sell = -1

#     i_cool = [2]
#        # decides i_cool = i or i + 1?
#         if prices[i] > last_sell:
#             i_cool.append(i+1)
#             last_sell = prices[i]
#             max_profit += prices[i] - last_sell
#         else
#             i_cool.append(i)
#             # last_sell not changed
#             # max_profit not changed

#         if 2 > 1:  # true
#             i_cool.append(2)
#             last_sell = 2
#             max_profit = 0 + 2 - 1 = 1
#     last_sell = 2
#     max_profit = 1

# [1, 2, 3]
#     i_cool = [2 ,3]
#         # decides i_cool = i or i + 1?
#         if prices[i] > last_sell:
#             i_cool.append(i+1)
#             last_sell = prices[i]
#             max_profit += prices[i] - last_sell
#         else
#            i_cool.append(i)
#             # last_sell not changed
#             # max_profit not changed

#         if 3 > 2:  # true
#             i_cool.append(3)
#             last_sell = 3
#             max_profit = 1 + 3 - 2 = 2

#     last_sell = 3
#     max_profit = 2

# [1, 2, 3, 0]
#     i_cool = [2 ,3, 3]
#         # decides i_cool = i or i + 1?
#         if prices[i] > last_sell:
#             i_cool.append(i+1)
#             last_sell = prices[i]
#             max_profit += prices[i] - last_sell
#         else
#            i_cool.append(i)
#             # last_sell not changed
#             # max_profit not changed

#         if 0 > 3:  # false
#         else
#             i_cool.append(3)

#     last_sell = 3
#     max_profit = 2
# [1, 2, 3, 0, 2]
#     i_cool = [2 ,3, 3]
#         # decides i_cool = i or i + 1?
#         if prices[i] > last_sell:
#             i_cool.append(i+1)
#             last_sell = prices[i]
#             max_profit += prices[i] - last_sell
#         else
#            i_cool.append(i)
#             # last_sell not changed
#             # max_profit not changed

#         if 0 > 3:  # false
#         else
#             i_cool.append(3)

#     last_sell = 3
#     max_profit = 2

# [1, 2, 3, 0, 2, 5]
#    max_profit = 5
#        i_cool = 5


# [1, 2, 3, 0, 2, 5]
# [1]
#     i_cooldown is a dict {i: max_profit}, where
#     i is when cooldown happens,
#     max_profit is the max_profit accumulated before that cooldown

#     i_cooldown: {}
#     final max_profit is max_profit of max(i) in i_cooldown or max(0,prices[0] - prices[-1])
#     max_profit = 0
#     last_buy = prices[i] = 1
# [1, 2]
# i = 1
#     if prices[i] - last_buy > 0:
#         i_cooldown.add(
#             {i+1: prices[i] - last_buy}
#         )
#     if 2 - 1 > 0: # true
#         i_cooldown = {
#             2: 1
#         }
#     max_profit = i_cooldown[max(i)] = 1
#     last_buy = 1

# [1, 2, 3]
# i = 2
#     # compare i_cooldown[i] vs prices[i] - last_buy:
#     if i_cooldown[i] > prices[i] - last_buy: #  if profit at cooldown at i is better than using prices[i] as sale point => do nothing
#         i_cooldown.add(
#             {i+1: prices[i] - last_buy}
#         )
#     else:
#         i_cooldown.add(
#             {i+1: prices[i] - last_buy}
#         )
#     if i_cooldown[2] > 3 - 1
#     if 1 > 2 # false
#     else:
#         i_cooldown.add(
#             {3: 3 - 1}
#         )

#     i_cooldown= {
#         2: 1
#         3: 2
#     }
#     max_profit = i_cooldown[max(i)] = i_cooldown[3] = 2
#     last_buy = 1

# [1, 2, 3, 0]
# i = 3
#     # compare i_cooldown[i] vs prices[i] - last_buy:
#     if i_cooldown[i] > prices[i] - last_buy: #  if profit at cooldown at i is better than using prices[i] as sale point => do nothing
#         i_cooldown.add(
#             {i+1: prices[i] - last_buy}
#         )
#     else:
#         i_cooldown.add(
#             {i+1: prices[i] - last_buy}
#         )
#     if i_cooldown[3] > 0 - 1
#     if 2 > -1 # true
#         i_cooldown.add(
#             4: -1
#         )

#     i_cooldown= {
#         2: 1
#         3: 2
#         4: -1
#     }
#     max_profit = i_cooldown[max(i)] = i_cooldown[3] = 2
#     last_buy = 1

# [1, 2, 3, 0, 2]
# i = 4
#     # compare i_cooldown[i] vs prices[i] - last_buy:
#     if i_cooldown[i] > prices[i] - last_buy: #  if profit at cooldown at i is better than using prices[i] as sale point => do nothing
#         i_cooldown.add(
#             {i+1: prices[i] - last_buy}
#         )
#     else:
#         i_cooldown.add(
#             {i+1: prices[i] - last_buy}
#         )
#     if i_cooldown[4] > 2 - 1
#     if -1 > 1 # false
#         i_cooldown.add(
#             5: 1
#         )

#     i_cooldown= {
#         2: 1
#         3: 2
#         4: -1
#         5: 1 # <== wrong, i_cooldown[5] = 3
#     }
#     max_profit = i_cooldown[max(i)] = i_cooldown[3] = 2
#     last_buy = 1

# [1, 2, 3, 0, 2, 5]


# [1, 2, 3, 0, 2, 5]
# [1]
#     i_cooldown is a dict {i: {max_profit:, last_buy:}, where
#         i is when cooldown happens,
#         max_profit is the max_profit accumulated before that cooldown
#         last_buy: buy price with respect to max_profit

#     i_cooldown: {}
#     max_profit = 0
#     last_buy = prices[i] = 1
# [1, 2]
# i = 1
#     i_cooldown = {
#         1: {
#             max_profit: 0
#             last_buy: 1
#         }
#     }
#     max_profit = max_profit + max(0,prices[i] - prices[i-1])

# [1, 2, 3]
# i = 2
#     max_profit = 2

#     max_profit = max(prices[i] - i_cooldown[j].last_buy + i_cooldown[j].max_profit for j in i_cooldown)
#     max_profit = max(3 - 1 + 0) = 2

#         i_cooldown = {
#         1: {
#             max_profit: 0
#             last_buy: 1
#         }
#         2: {
#             max_profit: 1
#             last_buy: 2
#         }
#     }

# [1, 2, 3, 0]
# i = 3
#     max_profit = 2
#     max_profit = max(prices[i] - i_cooldown[j].last_buy + i_cooldown[j],max_profit for j in i_cooldown, )
#     max_profit = max(0 - 1 + 0, 0 - 1 + 1) = max(-1, 0 ) = 0

#     i_cooldown = {
#         1: {
#             max_profit: 0
#             last_buy: 1
#         }
#         2: {
#             max_profit: 1
#             last_buy: 1
#         }
#         3:{
#             max_profit: 2
#             last_buy: 0
#         }
#     }

# [1, 2, 3, 0, 2]
# i = 4

#     max_profit = max(prices[i] - i_cooldown[j].last_buy + i_cooldown[j],max_profit for j in i_cooldown)

#     i_cooldown = {
#         1: {
#             max_profit: 0
#             last_buy: 1
#         }
#         2: {
#             max_profit: 1
#             last_buy: 1
#         }
#         3:{
#             max_profit: 2
#             last_buy: 0
#         }
#         4:{
#             max_profit:
#         }
#     }

# [1, 2, 3, 0, 2, 5]

# [1, 2, 3, 0, 2, 5]
# # initial state when len(prices) < 3
# [1]
#     max_profit_dict is a dict {i: {max_profit:, last_buy:}, where
#         i is when sale happens,
#         max_profit is the max_profit accumulated at that sale
#         last_buy: buy price with respect to max_profit

#     max_profit_dict: {
#         0: {
#             max_profit: 0
#             last_buy: 1
#         }
#     }
#     max_profit = 0
#     last_buy = prices[i] = 1
# [1, 2]
# # initial state when len(prices) < 3
# i = 1
#     max_profit_dict = {
#         0: {
#             max_profit: 0
#             last_buy: 1
#         },
#         1: {
#             max_profit: 1
#             last_buy: 1
#         }
#     }

#     max_profit[1].max_profit = max(0,prices[i] - prices[i-1])
#     max_profit[1].last_buy = max(prices[i],prices[i-1])

# [1, 2, 3]
# i = 2
# # DP loop when len(prices) >= 3
#     max_profit = max_profit_dict[i-1].max_profit + max(0, prices[i] - prices[i-1] + max_profit_dict[i-1].max_profit)
#     max_profit = 1 + max(0, 3 - 2 + 1) = 1 + 1 = 2

#         i_cooldown = {
#         0: {
#             max_profit: 0
#             last_buy: 1
#         },
#         1: {
#             max_profit: 1
#             last_buy: 1
#         }
#         2: {
#             max_profit: 2
#             last_buy: 1
#         }
#     }

# [1, 2, 3, 0]
# i = 4
# # DP loop when len(prices) >= 3
#     max_profit = max_profit_dict[i-1].max_profit + max(0, prices[i] - prices[i-1] + max_profit_dict[i-1].max_profit)
#     max_profit = 2 + max(0, 0 - 3 + 2) = 2 + 0 = 2

#         i_cooldown = {
#         0: {
#             max_profit: 0
#             last_buy: 1
#         },
#         1: {
#             max_profit: 1
#             last_buy: 1
#         }
#         2: {
#             max_profit: 2
#             last_buy: 1
#         },
#         3: {
#             max_profit: 2
#             last_buy: 1
#         }

#     }

# [1, 2, 3, 0, 2]
# i = 4

# [1, 2, 3, 0, 2, 5]
# # using machine state:
#   -----------------
#  |                 |
#  v                 |
# buy --> sell --> cool
#  ^        ^        ^
#  |        |        |
#  |        |        |
# hold_buy hold_sell keep_cool

# [1, 2, 3]

# buy = min(prices[i], buy) # decide between buy at prices[i] or previous minimum buy
# sell = max(prices[i] - buy)

# [1, 2, 3, 0, 2, 5]
# at each i there are 4 options:
#     - do_nothing
#     - buy if is_cooldown == false: cash -= prices[i], stock = prices[i]
#     - sell:  cash += prices[i]; stock = 0; is_cooldown = true
#     - cooldown: do_nothing; i_cooldown = False
# max_profit = max(cash)

#     do_nothing: liquid = liquid[i-1]; stock = stock[i-1]; is_cooldown = is_cooldown
#     buy:
#         if is_cooldown == false:
#             liquid = liquid[i-1] - prices[i]; stock = prices[i]
#         if is_cooldown == true: # cooldown
#     sell: liquid = prices[i] - stock[i-1]; stock = 0; is_cooldown = true
#     cooldown: liquid = liquid[i-1]; stock = stock[i-1], is_cooldown = false

#     max_profit = max(liquid)

# [1,2]
# i = 2
# liquid_if_not_cooldown = 1; stock_if_not_cooldown = -1 # liquid and stock value if cooldown supposedly not at i
# liquid_if_cooldown = 0; stock_if_cooldown = 0

# [1,2,3]
#     do_nothing:
#         liquid_if_not_cooldown = 1; stock_if_not_cooldown = 1
#         liquid_cooldown = 0; stock_if_cooldown = 0
#     buy:
#         stock_if_not_cooldown = max(stock_if_not_cooldown, liquid_if_cooldown - prices[i], liquid_if_not_cooldown - prices[i])
#         stock_if_not_cooldown = max(0, 0 - 3, 1 - 3) = 0
#         stock_if_cooldown = stock_if_not_cooldown[i-1] = -1
#     sell:
#         liquid = liquid[i-1] + prices[i];
#         liquid = 1 + 3 = 4

#     cooldown:
#         liquid = liquid[i-1];
#         liquid = 1
#         stock = stock[i-1];
#         stock = 2
#         is_cooldown = false


# [1, 2, 3, 0, 2, 5]
# at each i, if prices[i] is cooldown:
#     liquid_cooldown =

# [1]
# liquid = max(0, -inf + 1) = 0
# stock = max(-inf, 0 - 1) = -1
# is_cooldown = False
# [1, 2]
# buy:
#     if is_cooldown:
#         # do_nothing;
#         is_cooldown = False
#     else:
#         stock = max(stock[i-1], liquid[i-1] - prices[i])
#     if is_cooldown:  # False
#     else stock = max(-1, 0 - 2) = -1
#     sell:
#     if stock[i-1] + prices[i] > liquid[i-1]:  # good to sell
#         liquid = stock[i-1] + prices[i]
#         is_cooldown = True
#     else
#     # liquid unchanced
#     if -1 + 2 > 0:  # True
#         liquid = -1 + 2 = 1
#         is_cooldown = True
# [1, 2, 3]
# buy:
#     if is_cooldown:
#         # do_nothing;
#         is_cooldown = False
#     else:
#         stock = max(stock[i-1], liquid[i-1] - prices[i])
#     if is_cooldown:  # True
#         stock = -1
#         is_cooldown = False
#     sell:
#     if stock[i-1] + prices[i] > liquid[i-1]:  # good to sell
#         liquid = stock[i-1] + prices[i]
#         is_cooldown = True
#     else
#     # liquid unchanced
#     if -1 + 3 > 1:  # True
#         liquid = -1 + 3 = 2
#         is_cooldown = True
# [1, 2, 3, 0]
# buy:
#     if is_cooldown:
#         # do_nothing;
#         is_cooldown = False
#     else:
#         stock = max(stock[i-1], liquid[i-1] - prices[i])
#     if is_cooldown:  # True
#         stock = -1
#         is_cooldown = False
#     sell:
#     if stock[i-1] + prices[i] > liquid[i-1]:  # good to sell
#         liquid = stock[i-1] + prices[i]
#         is_cooldown = True
#     else
#     # liquid unchanced
#     if -1 + 0 > 2:  # False
#     else:  # liquid unchanged
#         liquid = 2
# [1, 2, 3, 0, 2]
# buy:
#     if is_cooldown:
#         # do_nothing;
#         is_cooldown = False
#     else:
#         stock = max(stock[i-1], liquid[i-1] - prices[i])
#     if is_cooldown:  # False
#     else:
#         stock = max(-1, 2 - 2) = 0
#     sell:
#     if stock[i-1] + prices[i] > liquid[i-1]:  # good to sell
#         liquid = stock[i-1] + prices[i]
#         is_cooldown = True
#     else
#     # liquid unchanced
#     if -1 + 2 > 2:  # False
#     else:  # liquid unchanged
#         liquid = 2

'''
___
prev_hold = -inf
prev_not_hold = 0
prev_cooldown = 0

for i in range(0, len(prices)):
    prev_hold = cur_hold
    prev_not_hold = cur_not_hold
    prev_cooldown = cur_cooldown

    cur_hold = max(prev_hold, prev_cooldown - prices[i])
    cur_not_hold = max(prev_not_hold, prev_hold + prices[i])
    cur_cooldown = max(prev_cooldown, prev_not_hold)

[1]
i = 0
    prev_hold = -inf
    prev_not_hold = 0
    prev_cooldown = 0

    cur_hold = max(-inf, 0 - 1) = -1
    cur_not_hold = max(0, -inf + 1) = 0
    cur_cooldown = max(0, 0) = 0

[1, 2]
i = 1
    prev_hold = -1
    prev_not_hold = 0
    prev_cooldown = 0

    cur_hold = max(-1, 0 - 2) = -1
    cur_not_hold = max(0, -1 + 2) = 1
    cur_cooldown = max(0, 0) = 0
[1, 2, 3]
i = 2
    prev_hold = -1
    prev_not_hold = 1
    prev_cooldown = 0

    cur_hold = max(-1, 0 - 3) = -1
    cur_not_hold = max(1, -1 + 3) = 2
    cur_cooldown = max(0, 1) = 1
[1, 2, 3, 0]
i = 3
    prev_hold = -1
    prev_not_hold = 2
    prev_cooldown = 1

    cur_hold = max(-1, 1 - 0) = 1
    cur_not_hold = max(2, -1 + 0) = 2
    cur_cooldown = max(1, 2) = 2
[1, 2, 3, 0, 2]
i = 4
    prev_hold = 1
    prev_not_hold = 2
    prev_cooldown = 2

    cur_hold = max(1, 2 - 2) = 1
    cur_not_hold = max(2, 1 + 2) = 3
    cur_cooldown = max(2, 2) = 2
[1, 2, 3, 0, 2, 5]
i = 4
    prev_hold = 1
    prev_not_hold = 3
    prev_cooldown = 2

    cur_hold = max(1, 2 - 5) = 1
    cur_not_hold = max(3, 1 + 5) = 6
    cur_cooldown = max(2, 3) = 3

'''
