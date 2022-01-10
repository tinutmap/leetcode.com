# question link https://leetcode.com/problems/intersection-of-two-arrays-ii/
from typing import List
import collections


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # solution 1: using dict. OK performance
        # https://leetcode.com/submissions/detail/617206997/
        d = {}
        for num in nums1:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        res = []
        for num in nums2:
            if num in d and d[num] > 0:
                res.append(num)
                d[num] -= 1
        return res

        # # solution 2: improvement on solution 1 not much improvement
        # # https://leetcode.com/submissions/detail/617208095/
        # d = {}
        # if len(nums2) > len(nums1):
        #     nums1, nums2 = nums2, nums1
        # for num in nums1:
        #     # can be replaced with d[num] = d.get(num,0) + 1
        #     if num in d:
        #         d[num] += 1
        #     else:
        #         d[num] = 1
        # res = []
        # for num in nums2:
        #     if num in d and d[num] > 0:
        #         res.append(num)
        #         d[num] -= 1
        # return res

        # forum solution:
        # # https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82247/Three-Python-Solutions

        # counts = collections.Counter(nums1)
        # res = []

        # for num in nums2:
        #     if counts[num] > 0:
        #         res += num,
        #         counts[num] -= 1

        # return res
        #
        # additional answer to follow up questions
        # # https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/1468295/Python-2-approaches-and-3-Follow-up-Questions-Clean-and-Concise
