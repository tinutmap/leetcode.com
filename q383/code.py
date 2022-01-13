# question link
class Solution:
    # solution 1: methodical approach. inferior performance
    #  https://leetcode.com/submissions/detail/619107312/
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for ch in magazine:
            d[ch] = d.get(ch, 0) + 1

        for ch in ransomNote:
            if ch not in d or d[ch] == 0:
                return False
            else:
                d[ch] -= 1

        return True

    # forum solution:
    # good one using counter:
    # https://leetcode.com/problems/ransom-note/discuss/85837/O(m%2Bn)-one-liner-Python
    # more of counter applications:
    # https://rahmonov.me/posts/python-collections-counter/
