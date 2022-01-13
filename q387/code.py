# question link https://leetcode.com/problems/first-unique-character-in-a-string/
import math


class Solution:
    # # solution 1: so-so performance
    # # https://leetcode.com/submissions/detail/619080135/
    # def firstUniqChar(self, s: str) -> int:
    #     d = {}
    #     # d = set()
    #     # s = set()
    #     # res = -1
    #     for i, ch in enumerate(s):
    #         if ch not in d:
    #             d[ch] = i
    #         else:
    #             d[ch] = len(s)
    #     res = min(d.values())
    #     return res if res < len(s) else -1

    # solution 2: based on solution 1. looping the string backward. Not much improvement
    # https://leetcode.com/submissions/detail/619082237/
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, ch in enumerate(s[-1::-1]):
            if ch not in d:
                d[ch] = i
            else:
                d[ch] = -1
        res = max(d.values())
        return res if res == -1 else len(s) - res - 1

    # # forum solution:
    # # use set 'seen' to keep track of repeated char
    # # https://leetcode.com/problems/first-unique-character-in-a-string/discuss/169270/Simple-Python
    # # from Python 3.7+ dict is now able to keep track of order of insertion
    # # https://leetcode.com/problems/first-unique-character-in-a-string/discuss/169270/Simple-Python/529042
    # def firstUniqChar(self, s):
    #     d = {}
    #     seen = set()
    #     for idx, c in enumerate(s):
    #         if c not in seen:
    #             d[c] = idx
    #             seen.add(c)
    #         elif c in d:
    #             del d[c]
    #     return next(iter(d.values())) if d else -1
    # # other way using the whole 26 char list. debatable o(n) but Python performance is good.
    # # https://leetcode.com/problems/first-unique-character-in-a-string/discuss/86351/Python-3-lines-beats-100-(~-60ms)-!
