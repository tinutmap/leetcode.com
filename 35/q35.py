# https://leetcode.com/problems/search-insert-position/

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    if target <= nums[l]:
        return l
    elif target == nums[r]:
        return r
    elif target > nums[r]:
        return r + 1
    else:
        while l < r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid
    return r


searchInsert([1, 3, 5, 6], target=5)
searchInsert([1, 3, 5, 6], target=2)
searchInsert([1, 3, 5, 6], target=7)
searchInsert([1, 3, 5, 6], target=0)
searchInsert([1], target=0)


# [1, 3, 5, 6]
# l = 0
# r = len(nums) -1

#     if target <= nums[l]:
#         return l
#     elif target >= nums[r]:
#         return r+1
#     else:
#         while l<r:
#             mid = l + (r - l) //2
#             if target == nums[mid]:
#                 return mid
#             elif target > nums[mid]:
#                 l = mid
#             else:
#                 r = mid

#     return r

# [1, 3, 5, 6], target=5
#     l = 0
#     r = 3

#         while 0 < 3: # True
#             mid = 0 + (3 - 0) // 2 = 1
#             if 5 == nums[1] == 3 # False
#             elif 5 > 3: # True
#                 l = 1 + 1  = 2
#     l = 2
#     r = 3

#         while 2 < 3: # True
#             mid = 2 + (3 - 2) // 2 = 2
#             if 5 == nums[2] == 5 # True
#                 return 2 # Correct

# [1, 3, 5, 6], target=2
#     l = 0
#     r = 3

#         while 0 < 3: # True
#             mid = 0 + (3 - 0) // 2 = 1
#             if 2 == nums[1] == 3 # False
#             elif 2 > 3: # False
#             else:
#                 r = 1

#     l = 0
#     r = 1

#         while 0 < 1: # True
#             mid = 0 + (1 - 0) // 2 = 0
#             if 2 == nums[0] == 1 # False
#             elif 2 > nums[0] = 1 # True
#                 l = 0 + 1 = 1

#     l = 1
#     r = 1
#         while 1 < 1: # False
#         return 1 # Correct

# [1, 3, 5, 6], target=0
#     l = 0
#     r = 3

#         while 0 < 3: # True
#             mid = 0 + (3 - 0) // 2 = 1
#             if 2 == nums[1] == 3 # False
#             elif 0 > 3: # False
#             else:
#                 r = 1

#     l = 0
#     r = 1

#         while 0 < 1: # True
#             mid = 0 + (1 - 0) // 2 = 0
#             if 0 == nums[0] == 1 # False
#             elif 0 > nums[0] = 1 # False
#             else:
#                 r = 0

#     l = 1
#     r = 0
#         while 1 < 0: # False
#         return 1 # False

# [1, 3, 5, 6], target=7
#     l = 0
#     r = 3

#         while 0 < 3: # True
#             mid = 0 + (3 - 0) // 2 = 1
#             if 6 == nums[1] == 3 # False
#             elif 6 > 3: # True
#                 l = 1 + 1 = 2

#     l = 2
#     r = 3

#         while 2 < 3: # True
#             mid = 2 + (3 - 2) // 2 = 2
#             if 7 == nums[2] == 5 # False
#             elif 7 > nums[3] = 5 # True
#                 l = 2 + 1 = 3

#     l = 3
#     r = 3
#         while 4 < 3: # False
#         return 1 # False
