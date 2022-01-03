# https://leetcode.com/problems/combinations/
from typing import List


class Solution:
    # # Solution 1: inferior solution
    # # https://leetcode.com/submissions/detail/609306395/
    # # improved with all_count
    # # https://leetcode.com/submissions/detail/609336920/
    # def combine(self, n: int, k: int) -> List[List[int]]:

    #     n_minus_k_fact = 1
    #     for i in range(2, n-k+1):
    #         n_minus_k_fact *= i

    #     n_fact_divide_k_fact = 1
    #     for i in range(k+1, n+1):
    #         n_fact_divide_k_fact *= i

    #     all_count = n_fact_divide_k_fact//n_minus_k_fact
    #     res = []
    #     all_res = res.copy()

    #     def recurse(start, stack):
    #         nonlocal all_count
    #         stack += 1
    #         if stack <= k:
    #             for i in range(start, n+1):
    #                 res.append(i)
    #                 recurse(i+1, stack)
    #                 res.pop()
    #             stack -= 1
    #         else:
    #             all_count -= 1
    #             all_res.append(res.copy())

    #             if all_count == 0:
    #                 return all_res

    #     recurse(1, 0)
    #     return all_res

    # Solution 2: improved on solution 1
    # used range(start, n+1-k+stack): in for loop to cut unnecessary loops
    # https://leetcode.com/submissions/detail/612383314/
    def combine(self, n: int, k: int) -> List[List[int]]:
        # first way of storing list
        res = [None] * k
        all_res = []
        # # second way of storing list: inferior
        # res = []
        # all_res = res.copy()

        def recurse(start, stack):
            stack += 1
            if stack <= k:
                for i in range(start, n+1-k+stack):
                    res[stack-1] = i
                    # res.append(i)
                    recurse(i+1, stack)
                    # res.pop()
                stack -= 1
            else:
                all_res.append(res.copy())
        recurse(1, 0)
        return all_res

    # # Forum solution: backtracking
    # def combine(self, n, k):
    #     ans = []
    #     stack = []
    #     x = 1
    #     while True:
    #         l = len(stack)
    #         if l == k:
    #             ans.append(stack[:])
    #         if l == k or x > n - k + l + 1:
    #             if not stack:
    #                 return ans
    #             x = stack.pop() + 1
    #         else:
    #             stack.append(x)
    #             x += 1
