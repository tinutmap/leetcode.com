# https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    # solution 1: accepted. People are damn optimized on solution so this is at the bottom :(
    # https://leetcode.com/submissions/detail/613751084/
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        res = [0] * n
        res[0] = nums[0]
        if n > 1:
            res[1] = max(nums[0], nums[1])
        for i in range(2, n):
            res[i] = max(res[i-2]+nums[i], res[i-1])
        return res[n-1]

    # # forum solution: good space optimized solution
    # # https://leetcode.com/problems/house-robber/discuss/1605797/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP
    # def rob(self, A):
    #     prev2, prev, cur = 0, 0, 0
    #     for i in A:
    #         cur = max(prev, i + prev2)
    #         prev2 = prev
    #         prev = cur
    #     return cur
