# https://leetcode.com/problems/rotate-array/

from typing import List


def rotate(nums: List[int], k: int) -> None:
    # solution 1:
    l = len(nums)
    k = k % l
    nums[:] = nums[-k:l] + nums[0:l-k]
    # ___
    # solution 2
    # l = len(nums)
    # k = k % l
    # nums.extend(nums[0:l-k])

    # popping the list from 0 to l-k

    # manual loop
    # for _ in range(l-k):
    #     nums.pop(0)

    # use del statement

    # del nums[0:l-k]

    # print(nums)
    # ___

    # wrong, this is rotating left
    # l = len(nums)
    # for _ in range(max(l-k, k-l)):
    #     nums.append(nums[0])
    #     nums.pop(0)


rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
rotate(nums=[-1, -100, 3, 99], k=2)
rotate(nums=[1, 2, 3], k=4)
