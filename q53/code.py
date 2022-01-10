# question link https://leetcode.com/problems/maximum-subarray/
from typing import List
import math


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # solution 1: dynamic programming correct but inferior
        # https://leetcode.com/submissions/detail/615178579/
        # res = sum = -math.inf
        # for num in nums:
        #     sum = max(num, sum+num)
        #     res = max(sum, res)
        # return res

        # solution 2: Kadane's solution
        # https://leetcode.com/submissions/detail/616493810/
        # credit from forum solution https://leetcode.com/problems/maximum-subarray/discuss/1595097/JAVA-or-Kadane's-Algorithm-or-Explanation-Using-Image
        res, sum = -math.inf, 0
        for num in nums:
            # sum = max(num, sum+num)
            sum += num
            res = max(sum, res)
            sum = max(0, sum)
        return res

        # forum solutions:
        # https://leetcode.com/problems/maximum-subarray/discuss/1595195/C%2B%2BPython-7-Simple-Solutions-w-Explanation-or-Brute-Force-%2B-DP-%2B-Kadane-%2B-Divide-and-Conquer
