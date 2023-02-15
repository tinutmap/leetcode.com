# question link https://leetcode.com/problems/running-sum-of-1d-array/submissions/

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # solution 1: Satisfying solution.
        # solution link https://leetcode.com/problems/running-sum-of-1d-array/submissions/898748988/
        last_sum = 0
        # nums.insert(0, 0)
        for index, num in enumerate(nums):
            nums[index] = num + last_sum
            last_sum += num

        return nums

        # forum solution: better than solution 1
        # for i in range(1, len(nums)):
        #     nums[i] += nums[i-1]
        # return nums
        # solution link https://leetcode.com/problems/running-sum-of-1d-array/solutions/2699842/python-c-java-faster-than-100-simple-short-solution-2-line-solution/?languageTags=python
