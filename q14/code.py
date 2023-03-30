# question link
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # # solution 1:
        # # solution link

        # return 0

        # forum solution: good use of min with key.
        # solution link https://leetcode.com/problems/longest-common-prefix/solutions/6918/short-python-solution/
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
