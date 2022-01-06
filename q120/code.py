# https://leetcode.com/problems/triangle/
from typing import List
import math


class Solution:
    # # solution 1: inferior
    # # https://leetcode.com/submissions/detail/613828291/
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     n = len(triangle)
    #     res = triangle[0][0]
    #     for i in range(1, n):
    #         res = math.inf
    #         for j in range(len(triangle[i])):
    #             a = triangle[i-1][j] if j < i else math.inf
    #             b = triangle[i-1][j-1] if j > 0 else math.inf
    #             triangle[i][j] += min(a, b)
    #             res = min(res, triangle[i][j])
    #     return res

    # # solution 2: improvement upon solution 1
    # # https://leetcode.com/submissions/detail/613830785/
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     n = len(triangle)
    #     for i in range(1, n):
    #         for j in range(len(triangle[i])):
    #             a = triangle[i-1][j] if j < i else math.inf
    #             b = triangle[i-1][j-1] if j > 0 else math.inf
    #             triangle[i][j] += min(a, b)
    #     return min(triangle[-1])

    # solution 2: space O(n), not better than solution 2
    # https://leetcode.com/submissions/detail/613836613/
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = [*triangle[0]]+[math.inf]
        for i in range(1, len(triangle)):
            res = [math.inf]+res
            for j in range(len(triangle[i])):
                res[j] = triangle[i][j] + min(res[j], res[j+1])
        return min(res)

    # # forum solution: good collections of ways. performance comparable to \
    # # solution 2 and 3
    # # https://leetcode.com/problems/triangle/discuss/38735/Python-easy-to-understand-solutions-(top-down-bottom-up).
    # def minimumTotal(self, triangle):
    #     if not triangle:
    #         return
    #     res = triangle[-1]
    #     for i in range(len(triangle)-2, -1, -1):
    #         for j in range(len(triangle[i])):
    #             res[j] = min(res[j], res[j+1]) + triangle[i][j]
    #     return res[0]
