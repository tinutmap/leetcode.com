class Solution:

    """
    # Solution 1: passed but inferior https://leetcode.com/submissions/detail/598006662/
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        s1_list = list(s1)
        s1_list.sort()
        for i in range(l2-l1+1):
            sub_s2_list = list(s2[i:l1+i])
            sub_s2_list.sort()
            if sub_s2_list == s1_list:
                return True
        return False
    """

    """
    # Solution 2: passed convert letters to ASCII values, using list to track frequency
    # better idea but inferior performance https://leetcode.com/submissions/detail/598014077/
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False

        list_1 = [0] * 26
        list_2 = [0] * 26
        for l in s1:
            list_1[ord(l) - ord('a')] += 1

        for i in range(l2-l1+1):
            sub_s2 = s2[i:l1+i]
            list_2 = [0] * 26
            for l in sub_s2:
                list_2[ord(l) - ord('a')] += 1
            if list_1 == list_2:
                return True
        return False
    """

    # Solution 3: passed, improved from solution 2.
    # https://leetcode.com/submissions/detail/598017585/
    # credit: https://leetcode.com/problems/permutation-in-string/discuss/638531/Java-or-C%2B%2B-or-Python3-or-Detailed-explanation-or-O(N)-time
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False

        list_1 = [0] * 26
        for l in s1:
            list_1[ord(l) - ord('a')] += 1

        list_2 = [0] * 26
        sub_s2 = s2[0:l1-1]
        for l in sub_s2:
            list_2[ord(l) - ord('a')] += 1

        for i in range(l1-1, l2):
            list_2[ord(s2[i]) - ord('a')] += 1
            if list_1 == list_2:
                return True
            list_2[ord(s2[i-l1+1]) - ord('a')] -= 1
        return False
