# https://leetcode.com/problems/reverse-string/
from typing import List


def reverseString(s: List[str]) -> None:
    # python list comprehension
    # s[:] = s[-1:-1-len(s):-1]

    len_s = len(s)
    mid = len_s//2
    for i in range(0, mid):
        if s[i] != s[len_s - i - 1]:
            s[i], s[len_s - i - 1] = s[len_s-i-1], s[i]


reverseString(["h", "e", "l", "l", "o"])
reverseString(["H", "a", "n", "n", "a", "h"])
