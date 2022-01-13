# question link https://leetcode.com/problems/valid-anagram/
from collections import Counter


class Solution:
    # solution 1: using Counter. that's still inferior to you, folks!?
    # https://leetcode.com/submissions/detail/619123159/
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return not (Counter(s) - Counter(t))

    # few forum solutions:
    # https://leetcode.com/problems/valid-anagram/discuss/66499/Python-solutions-(sort-and-dictionary).
    # instead of substraction, we can compare counter:
    #         return Counter(s) == Counter(t)
