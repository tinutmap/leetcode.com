# question link https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    # # solution 1: inferior
    # # https://leetcode.com/submissions/detail/615135654/
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     return len(set(nums)) != len(nums)

    # # solution 2: inferior
    # # https://leetcode.com/problems/contains-duplicate/submissions/
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     nums.sort()
    #     for i in range(len(nums)-1):
    #         if nums[i] == nums[i+1]:
    #             return True
    #     return False

    # solution 3: using set: still inferior! this must not be, since best forum answer is the same
    # https://leetcode.com/submissions/detail/615145652/
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False

    # # solution 4: using dict
    # # still inferior
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     l = {}
    #     for num in nums:
    #         if num in l:
    #             return True
    #         else:
    #             l.update({num: None})
    #     return False
