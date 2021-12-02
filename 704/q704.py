# https://leetcode.com/problems/binary-search/

from typing import List
import math


def search(self, nums: List[int], target: int) -> int:
    len_nums = len(nums)
    target_index = -1
    upper_bound_index = len_nums - 1
    lower_bound_index = 0

    if target == nums[upper_bound_index]:
        target_index = upper_bound_index
    elif target == nums[lower_bound_index]:
        target_index = lower_bound_index
    else:
        mid_point_index = math.floor(
            (lower_bound_index + upper_bound_index)/2)
        while upper_bound_index >= lower_bound_index:
            if target == nums[mid_point_index]:
                target_index = mid_point_index
                break
            elif target > nums[mid_point_index]:
                lower_bound_index = mid_point_index + 1
            else:
                upper_bound_index = mid_point_index - 1
            mid_point_index = math.floor(
                (lower_bound_index + upper_bound_index)/2)
    return target_index


# search([-1, 0, 3, 5, 9, 12], 9)
# search([-1, 0, 3, 5, 9, 12], 7)
search([-1, 0, 3, 5, 9, 10, 12, 13], 12.5)


# [0, 1, 2, 3, 4, 5]
# l = 6
# mid_point_index = 3
# prices[mid_point_index] = 3
# target = 4
