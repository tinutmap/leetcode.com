# question link
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # solution 1:
        # https://leetcode.com/submissions/detail/615033275/
        res = 0
        for num in nums:
            res ^= num
        return res


# a = [0, 1, 2, 3, 3, 2, 1]
# a = [0, 12, 12, 13, 13, 14, 14, 2]
# res = 0
# for num in a:
#     res ^= num
# print(res)
