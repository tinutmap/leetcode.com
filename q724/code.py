# question link https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan&id=level-1
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # solution 1:
        # solution link
        right_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            right_sum -= num
            if left_sum == right_sum:
                return i
            left_sum += num

        return -1

        # forum solution: similar to solution 1, can combine var assignment
        #  total_weight_on_left, total_weight_on_right = 0, sum(nums)
        # solution link https://leetcode.com/problems/find-pivot-index/solutions/512992/python-go-java-js-c-o-n-sol-by-balance-scale-w-explanation/
