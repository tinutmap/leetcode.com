# https://leetcode.com/problems/letter-case-permutation/
from typing import List


class Solution:
    # # solution 1: performance not so good
    # # https: // leetcode.com/submissions/detail/613125845/
    # def letterCasePermutation(self, s: str) -> List[str]:
    #     char_index_list = [index for index in range(
    #         len(s)) if s[index].lower() >= 'a']
    #     l = len(char_index_list)
    #     res = []

    #     def recurse(index, s):
    #         if index < l:
    #             char_index = char_index_list[index]
    #             char = s[char_index].lower()
    #             for char_case in (char, char.upper()):
    #                 recurse(index+1, s[:char_index]+char_case+s[char_index+1:])
    #         else:
    #             res.append(s)

    #     recurse(0, s)
    #     return res

    # # solution 2: still inferior
    # # https://leetcode.com/submissions/detail/613130606/
    # def letterCasePermutation(self, s: str) -> List[str]:
    #     l = len(s)
    #     res = []

    #     def recurse(index, s):
    #         if index < l:
    #             char = s[index].lower()
    #             if char >= 'a':
    #                 for char_case in (char, char.upper()):
    #                     recurse(index+1, s[:index]+char_case+s[index+1:])
    #             else:
    #                 recurse(index+1, s)
    #         else:
    #             res.append(s)

    #     recurse(0, s)
    #     return res

    # forum solution: very brilliant, using debug for details!
    # isalpha() is a good way to test alphabet letter.
    # https: // leetcode.com/problems/letter-case-permutation/discuss/115509/Python-simple-solution-(7-lines)

    def letterCasePermutation(self, s):
        res = ['']
        for ch in s:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
        return res
