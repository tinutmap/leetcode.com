# question link https://leetcode.com/problems/min-cost-climbing-stairs/?envType=study-plan&id=level-1
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # # solution 1: OK solution. A bit fuzzy and messy with min_cost array that not space optimized. Time 37:03
        # # solution link https://leetcode.com/problems/min-cost-climbing-stairs/submissions/916318503/?envType=study-plan&id=level-1
        # l = len(cost)
        # if l <= 2:
        #     return min(cost)

        # # a, b = cost[0], cost[1]
        # min_cost = [0]*2
        # for i in range(2, l):
        #     min_cost.append(
        #         min(min_cost[-2]+cost[i-2], min_cost[-1]+cost[i-1]))
        # return min(min_cost[-2]+cost[l-2], min_cost[-1]+cost[l-1])

        # solution 2: OK solution, surpringly worse than solution 1. Based on solution 1, using a,b instead of a whole min_cost[] for space optimization.
        # solution link https://leetcode.com/problems/min-cost-climbing-stairs/submissions/916321141/?envType=study-plan&id=level-1
        if len(cost) <= 2:
            return min(cost)

        a, b = 0, 0
        for i in range(2, len(cost)):
            a, b = b,  min(a+cost[i-2], b+cost[i-1])
        return min(a+cost[-2], b+cost[-1])

        # forum solution: more orthodox and methodological explanation with recursion as well. Great to refresh DP
        # solution link https://leetcode.com/problems/min-cost-climbing-stairs/solutions/476388/4-ways-or-Step-by-step-from-Recursion-greater-top-down-DP-greater-bottom-up-DP-greater-fine-tuning/
