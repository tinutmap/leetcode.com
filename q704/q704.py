# https://leetcode.com/problems/binary-search/

from typing import List
import math


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # # Solution 1: inferior
        # # Solution link: https://leetcode.com/problems/binary-search/submissions/617690724/
        # len_nums = len(nums)
        # target_index = -1
        # upper_bound_index = len_nums - 1
        # lower_bound_index = 0

        # if target == nums[upper_bound_index]:
        #     target_index = upper_bound_index
        # elif target == nums[lower_bound_index]:
        #     target_index = lower_bound_index
        # else:
        #     mid_point_index = math.floor(
        #         (lower_bound_index + upper_bound_index)/2)
        #     while upper_bound_index >= lower_bound_index:
        #         if target == nums[mid_point_index]:
        #             target_index = mid_point_index
        #             break
        #         elif target > nums[mid_point_index]:
        #             lower_bound_index = mid_point_index + 1
        #         else:
        #             upper_bound_index = mid_point_index - 1
        #         mid_point_index = math.floor(
        #             (lower_bound_index + upper_bound_index)/2)
        # return target_index

        # Solution 2: better than solution 1, especiaLy memory but still inferior runtime. 2/21/2023
        # Solution link: https://leetcode.com/problems/binary-search/submissions/902646281/

        l, r = 0, len(nums)-1
        if target > nums[-1] or target < nums[0]:
            return -1

        while l+1 < r:
            # this prevents integer overflow in Java if both r and L are quite bi
            mid = l + (r - l) // 2
            if target >= nums[mid]:
                l = mid
            else:
                r = mid
        return l if nums[l] == target else r if nums[r] == target else -1

        # Forum Solution: similar way but may use l + 1 or r-1 for mid
        # Forum link: https://leetcode.com/problems/binary-search/solutions/1884068/python-javascript-easy-solution-with-very-clear-explanation/
