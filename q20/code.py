# question link https://leetcode.com/problems/valid-parentheses/
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        # solution 1: such a few mistakes due to being rushed. Edge cases are there to trap!
        # not so good TC but good SC.
        # solution link https://leetcode.com/submissions/detail/619149902/
        d = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        dq = deque([])
        for ch in s:
            if ch in d and dq:
                if dq.pop() != d[ch]:
                    return False
            else:
                dq.append(ch)
        return not dq

        # forum solution is similar:
        # https://leetcode.com/problems/valid-parentheses/discuss/316753/Python-4ms-Faster-then-100-with-explanation
        # few take away:
        # check if len(s) % 2 == 1: return False
        # can use regular list as stack
        #
