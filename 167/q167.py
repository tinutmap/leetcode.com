# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    # # solution 1: binary search LTE
    # numbers_len = len(numbers)
    # for l in range(0, numbers_len - 1):
    #     delta = target - numbers[l]
    #     mid = l + 1 + (numbers_len - l - 2) // 2
    #     if numbers[mid] >= delta:
    #         direction = -1
    #     else:
    #         direction = 1

    #     while l < mid and mid < numbers_len:
    #         if numbers[mid] == delta:
    #             return [l+1, mid+1]
    #         else:
    #             mid += direction

    # # solution 2: brute force:  LTE
    # for l in range(0, numbers_len):
    #     for i in range(l+1, numbers_len):
    #         if numbers[l] + numbers[i] == target:
    #             return [l+1, i+1]

    # # solution 3: improved from solution 1 - accepted but time O(n) is inferior
    # numbers_len = len(numbers)
    # for l in range(0, numbers_len - 1):
    #     delta = target - numbers[l]
    #     mid = l + 1 + (numbers_len - l - 2) // 2
    #     if numbers[mid] >= delta:
    #         while mid > l and numbers[mid] >= delta:
    #             if numbers[mid] == delta:
    #                 return [l+1, mid+1]
    #             else:
    #                 mid -= 1
    #     elif numbers[mid] <= delta:
    #         while mid < numbers_len and numbers[mid] <= delta:
    #             if numbers[mid] == delta:
    #                 return [l+1, mid+1]
    #             else:
    #                 mid += 1

    # # solution 4: divide numbers into 2 sub indices,
    # # find l_max where  numbers[l_max]<=target/2 =< numbers[l_max+1]
    # # Acceptable

    # numbers_len = len(numbers)

    # l_max = numbers_len // 2
    # if numbers[l_max] == target/2:
    #     if numbers[l_max - 1] == target/2:
    #         l_max -= 1
    # elif numbers[l_max] > target / 2:
    #     while l_max > 0 and numbers[l_max] >= target / 2:
    #         l_max -= 1
    # else:
    #     while l_max < numbers_len-1 and numbers[l_max] <= target / 2:
    #         l_max += 1
    #     l_max -= 1
    # r_min = l_max + 1
    # while True:
    #     for l in range(l_max, -1, -1):
    #         if numbers[l] + numbers[r_min] == target:
    #             return [l+1, r_min+1]
    #     for r in range(r_min, numbers_len):
    #         if numbers[l_max] + numbers[r] == target:
    #             return [l_max+1, r+1]

    #     l_max -= 1
    #     r_min += 1

    # solution 5: use dict
    numbers_len = len(numbers)
    dic = {}
    for i in range(numbers_len):
        if numbers[i] not in dic:
            dic[numbers[i]] = i
        delta = target - numbers[i]
        if delta in dic and i != dic[delta]:
            return [dic[delta]+1, i+1]

    # Other solutions https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51249/Python-different-solutions-(two-pointer-dictionary-binary-search).


twoSum(numbers=[2, 7, 11, 15], target=9)
twoSum(numbers=[2, 3, 4], target=6)
twoSum(numbers=[-1, 0], target=-1)
twoSum(numbers=[-4, -3, -2, -1, 0], target=-7)
twoSum(numbers=[5, 25, 75], target=100)
twoSum([3, 24, 50, 79, 88, 150, 345], 200)
twoSum([0, 0, 3, 4], 0)
twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8)
twoSum([1, 3, 4, 4], 8)


'''
whiteboard

using 2 pointers:
    l: index loops from index 0 up
    delta = target - numsbers[l]
    find delta in nums[l+1:len(numbers)] using binary search
    return [l + 1, delta_index]

[2, 7, 11, 15],
    l = 0
    delta = 9 - 2 = 7
    search 7 in [7, 11, 15]
        mid = l + 1 + (len(nums) - 1 - l - 1)//2
            = 0 + 1 + (4 - 1 -0 - 1)//2 = 2

        while l < mid and mid < len(nums):
            if numbers[mid] == delta:
                return [l + 1, mid + 1]
            if numbers[mid] > delta:
                mid -= 1
            else
                mid += 1
        while  0 < 2 and 2 < 4:
            numbers[2] = 11 > delta = 7
                mid = 2 - 1 = 1

        while 0 < 1 and 1 < 4: # True
            if numbers[1] = 7 == delta
                return [0 + 1, 1 + 1] = [1, 2]


[0, 0, 1, 2], 0
l_max = 2
    while l_max > 0 and numbers[l_max] >= target / 2:
        l_max -= 1
    
    while 2 > 0 and 1 >= 0:
        l_max = 1

    while 1>0 and 0 >= 0:
        l_max = 0
    while 0 > 0 and 0>=0: False

    l_max = 0 # Correct


[2, 3, 4, 5, 5], 10
l_max = 2
    if 4 > 5: # False
        while l_max < numbers_len-1 and numbers[l_max] <= target / 2:
            l_max += 1
        l_max -= 1

        while 2 < 4 and 4 <= 5:
            l_max = 3
        
        while 3 < 4 and 5<=5: # True
            l_max = 4
        
        while 4<4 and 5<=5: # False

        l_max = 3

[1, 3, 4, 4], 8
l_max = 2
    if 4 == 4: # False
        while l_max < numbers_len-1 and numbers[l_max] <= target / 2:
            l_max += 1
        l_max -= 1

        while 2 < 4 and 4 <= 5:
            l_max = 3
        
        while 3 < 4 and 5<=5: # True
            l_max = 4
        
        while 4<4 and 5<=5: # False

        l_max = 3

'''
