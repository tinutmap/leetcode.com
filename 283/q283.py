# https://leetcode.com/problems/move-zeroes/

from typing import List


def moveZeroes(nums: List[int]) -> None:
    count_0 = nums.count(0)
    if count_0 > 0 and len(nums) > 1:
        # # solutioin 1: append 0 to the end and pop 0 at 0's index: pass
        # for _ in range(count_0):
        #     index_0 = nums.index(0)
        #     nums.pop(index_0)
        #     nums.append(0)

        # # solution 2:
        # for _ in range(count_0):
        #     for i in range(nums.index(0), len(nums)-1):
        #         if nums[i+1] != 0:
        #             nums[i], nums[i+1] = nums[i+1], nums[i]

        # solution 3:
        good_id = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[good_id], nums[i] = nums[i], nums[good_id]
                good_id += 1


moveZeroes([0, 1, 0, 3, 12])
moveZeroes([0])
