# question link https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=study-plan&id=level-1
from typing import List
import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # # solution 1: naive! stack overflown!
        # # solution link
        # re = []
        # p_length, s_length = len(p), len(s)
        # if p_length > s_length:
        #     return re
        # p_sorted = ''.join(sorted(p))
        # for i in range(0, s_length-p_length+1):
        #     if ''.join(sorted(s[i:i+p_length])) == p_sorted:
        #         re.append(i)

        # return re

        # solution 2: very messy but got the point. time 01 : 04 : 46!
        # solution link https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/916927238/?envType=study-plan&id=level-1
        re = []
        p_length, s_length = len(p), len(s)
        if p_length > s_length:
            return re

        p_map = {}

        for char in p:
            if char not in p_map:
                p_map[char] = 1
            else:
                p_map[char] += 1

        # first pass
        s_ = collections.deque(s[0:p_length])
        for char in s_:
            if char in p_map:
                p_map[char] -= 1
        if list(p_map.values()).count(0) == len(p_map.keys()):
            re.append(0)

        for i in range(p_length, s_length):
            l_char = s_.popleft()
            if l_char in p_map:
                p_map[l_char] += 1
            s_.append(s[i])
            if s[i] in p_map:
                p_map[s[i]] -= 1
            if list(p_map.values()).count(0) == len(p_map.keys()):
                re.append(i-p_length+1)
        return re
        # forum solution:
        # solution link
