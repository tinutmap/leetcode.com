# question link
from typing import List
import math


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # # solutuion 1: why the zeros there!!!
        # # https://leetcode.com/submissions/detail/617098752/

        # if m == 0:
        #     for i in range(n):
        #         nums1[i] = nums2[i]
        # elif n == 0:
        #     pass
        # else:
        #     k = len(nums1)-1
        #     while len(nums1) != m:
        #         if nums1[k] == 0:
        #             nums1.pop(k)
        #             # m -= 1
        #         k -= 1
        #     i = j = 0
        #     nums1.append(math.inf)
        #     nums1.insert(0, -math.inf)
        #     while i < len(nums1)-1:
        #         while j < n and nums1[i] <= nums2[j] <= nums1[i+1]:
        #             nums1.insert(i+1, nums2[j])
        #             j += 1
        #         i += 1
        #     nums1.pop()
        #     nums1.remove(-math.inf)

        # # solution 2: based on solution 1
        # # https://leetcode.com/submissions/detail/617189995/
        # i = j = 0
        # if m < len(nums1):
        #     nums1[m] = math.inf
        # else:
        #     nums1.append(math.inf)
        # nums1.insert(0, -math.inf)
        # while i < n+m:
        #     while j < n and nums1[i] <= nums2[j] <= nums1[i+1]:
        #         nums1.insert(i+1, nums2[j])
        #         j += 1
        #     i += 1
        # temp = nums1[1:n+m+1]
        # nums1.clear()
        # nums1.extend(temp)

        # solution 3: credit forum solution
        # https://leetcode.com/problems/merge-sorted-array/discuss/29503/Beautiful-Python-Solution
        while n > 0 and m > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        nums1[:n] = nums2[:n]
