# https://leetcode.com/problems/squares-of-a-sorted-array/
from typing import List
# import math


def sortedSquares(nums: List[int]) -> List[int]:
    # wrong answer
    # if nums[-1] <= 0:
    #     result = [nums[j]**2 for j in range(len(nums)-1, -1, -1)]
    # elif nums[0] >= 0:
    #     result = [nums[j]**2 for j in range(0, len(nums))]
    # else:
    #     mid = len(nums) // 2
    #     result = []
    #     for i in range(mid, len(nums)):
    #         a = abs(nums[i])
    #         b = abs(nums[len(nums)-i - 1])
    #         if a > b:
    #             result.append(b**2)
    #             result.append(a**2)
    #         elif a < b:
    #             result.append(a**2)
    #             result.append(b**2)
    #         else:  # a==b
    #             if i > len(nums) - i - 1:  # append another if 2 disticnt index
    #                 result.append(a**2)
    #             result.append(a**2)

    l_index = 0
    r_index = len(nums) - 1
    # this method instead of using list.insert increases much better computing cost.
    result = [0] * len(nums)
    i = len(nums) - 1
    while l_index <= r_index:
        if abs(nums[l_index]) >= abs(nums[r_index]):
            result[i] = nums[l_index]**2
            l_index += 1
        else:
            result[i] = nums[r_index]**2
            r_index -= 1
        i -= 1
    return result


sortedSquares(nums=[-4, -1, 0, 3, 10])
sortedSquares(nums=[-7, -3, 2, 3, 11])
sortedSquares(nums=[-4, -1, 3, 10])
sortedSquares(nums=[-10, -4, -3, -1])
sortedSquares(nums=[1, 3, 4, 10])
sortedSquares(nums=[-10000, -9999, -7, -5, 0, 0, 10000])

# i = 3
# -1 index = 1 ==> len(nums) - 3

# i =4
# -4 index - 0 --> len(nums) - 4
