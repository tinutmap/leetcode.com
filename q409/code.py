# question link https://leetcode.com/problems/longest-palindrome/description/

import collections
from functools import reduce


class Solution:
    def longestPalindrome(self, s: str) -> int:

        # solution 1: OK solution
        # solution link https://leetcode.com/problems/longest-palindrome/submissions/901851762/

        d = collections.Counter(s).values()
        res = sum([count if count % 2 == 0 else count-1 for count in d])
        res += res < sum(d)
        return res

# forum solution: some one-liner sh*t for reference.
# solution link https://leetcode.com/problems/longest-palindrome/solutions/89587/what-are-the-odds-python-c/
