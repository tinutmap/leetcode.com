# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # solution 1: first tried in 9/17/2021
        # # https://leetcode.com/submissions/detail/556596577/
        # result = set()
        # for x in range(len(nums)):
        #     y = target - nums[x]
        #     if y in nums:
        #         y_index = nums.index(y)
        #         if y_index != x:
        #             result.update([x,y_index])
        # return list(result)

        # solution 2: using dict so-so performance. Revisited after long while doing solution 1
        # this is matching forum solution! Feel great!
        # https://leetcode.com/submissions/detail/617032393/
        d = {}
        for index, val in enumerate(nums):
            if (m := target-val) in d:
                return [d[m], index]
            # if val not in d:
            #     d.update({val: index})
            d[val] = index
