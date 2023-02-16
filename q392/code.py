# question link https://leetcode.com/problems/is-subsequence/description/?envType=study-plan&id=level-1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # solution 1: follow algorithm done in JS. Great runtime but not so good memory.
        # solution link https://leetcode.com/problems/is-subsequence/submissions/899391765/?envType=study-plan&id=level-1
        left_index_t = 0
        for char in s:
            new_left_index_t = t.find(char, left_index_t)
            if new_left_index_t < left_index_t:
                return False
            left_index_t = new_left_index_t+1
        return True

        # # solution 2: 2-pointer, is it? Or another version of solution 1. Can't get my head away from solution 1?
        # # solution link https://leetcode.com/problems/is-subsequence/submissions/899398688/?envType=study-plan&id=level-1
        # j = 0
        # for char in s:
        #     j_temp = j
        #     while j_temp < len(t):
        #         if char == t[j_temp]:
        #             j = j_temp+1
        #             break
        #         else:
        #             j_temp += 1
        #     if j_temp == len(t):
        #         return False
        # return True

        # # forum solution: real 2 pointer here https://leetcode.com/problems/is-subsequence/solutions/2473010/very-easy-100-fully-explained-java-c-python-js-c-python3-two-pointers-approach/
        # # God-liked Python solution here: https://leetcode.com/problems/is-subsequence/solutions/87258/2-lines-python/
        # remainder_of_t = iter(t)
        # for letter in s:
        #     if letter not in remainder_of_t:  # can't find way to print remainder_of_t without hurting __next__ of iter to see how iter removes letter
        #         return False

        # return True
