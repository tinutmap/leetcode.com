class Solution:
    """
    # solution 1: LTE
    def is_palindrome(self, sub_s):
        i, j = 0, len(sub_s)-1
        # palindrome = True
        while i < j:
            if sub_s[i] != sub_s[j]:
                return False
            i += 1
            j -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        d = {}
        sub_s = ''
        best_sub_s = s[0]
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i]
            else:
                for last_pos in d[s[i]]:
                    # last_pos = d[s[i]]
                    sub_s = s[last_pos:i+1]
                    if self.is_palindrome(sub_s) and len(sub_s) > len(best_sub_s):
                        best_sub_s = sub_s
                d[s[i]].append(i)

        return best_sub_s
    """
    # solution 2: seach each char and in between char:
    # https://leetcode.com/submissions/detail/598973728/

    def find_max_pal(self, l, r, s):
        # if s[l] == s[r]:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # if
            l = l - 1
            r = r + 1
            # else:
            #     break
        return s[l+1:r]
        # else:
        #     return ''

    def longestPalindrome(self, s: str) -> str:
        max_pal = s[0]
        for i in range(len(s)):
            # odd case, palindrom with one char in the center
            s1 = self.find_max_pal(i-1, i+1, s)
            # odd case, palindrom with no char in the center
            s2 = self.find_max_pal(i, i+1, s)
            if len(s1) < len(s2):
                s1, s2 = s2, s1
            if len(s1) > len(max_pal):
                max_pal = s1
        return max_pal

    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """

    #     res = ""
    #     for i in range(len(s)):
    #         res = max(self.helper(s, i, i), self.helper(
    #             s, i, i+1), res, key=len)

    #     return res

    # def helper(self, s, l, r):

    #     while 0 <= l and r < len(s) and s[l] == s[r]:
    #         l -= 1
    #         r += 1
    #     return s[l+1:r]


"""
solutions:
- https://leetcode.com/problems/longest-palindromic-substring/solution/
- https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).
- https://leetcode.com/problems/longest-palindromic-substring/discuss/900639/Python-Solution-%3A-with-detailed-explanation-%3A-using-DP

Key takeaway:
- Easiest to understand is using expanding around center
- DP is also understandable using 2D matrix but requires more code.
- in `while` loop when there are multiple conditions, they are evaluated left to right:
    - e.g. `while l >= 0 and r < len(s) and s[l] == s[r]:` throws no exception when s[l] or s[r] is out of index
    - otherwise `while s[l] == s[r] and l >= 0 and r < len(s)` throws exception

- max() has key argument 
"""
