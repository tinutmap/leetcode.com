# question link
from operator import itemgetter


class Solution:
    def decodeString(self, s: str) -> str:
        # solution 1: need 2 sessions of 45 mins with a few hours in between to figure out. Great runtime, above average memory. Using recursive
        # solution link https://leetcode.com/problems/decode-string/submissions/921011266/

        def recurse(s: str):
            st = ''
            k = ''
            i = 0
            while i < len(s):
                if s[i].isalpha():
                    st += s[i]
                    i += 1
                elif s[i].isnumeric():
                    k += s[i]
                    i += 1
                elif s[i] == '[':
                    sub_st, sub_st_l = itemgetter(
                        'st', 'i')(recurse(s[i+1:]))
                    st += int(k)*sub_st
                    k = ''
                    i += sub_st_l
                else:
                    # return {'sub_st': st, 'sub_st_l': i+2} # example of returning keyword values rather than list of values
                    return {'st': st, 'i': i+2}
            return st

        return recurse(s)

        # # forum solution: using stack. Worse than solution 1's runtime but much better with memory.
        # # result: https://leetcode.com/problems/decode-string/submissions/921341362/?envType=study-plan&id=level-1
        # # solution link https://leetcode.com/problems/decode-string/solutions/941309/python-stack-solution-explained/
        # it, num, stack = 0, 0, [""]
        # while it < len(s):
        #     if s[it].isdigit():
        #         num = num * 10 + int(s[it])
        #     elif s[it] == "[":
        #         stack.append(num)
        #         num = 0
        #         stack.append("")
        #     elif s[it] == "]":
        #         str1 = stack.pop()
        #         rep = stack.pop()
        #         str2 = stack.pop()
        #         stack.append(str2 + str1 * rep)
        #     else:
        #         stack[-1] += s[it]
        #     it += 1
        # return "".join(stack)
