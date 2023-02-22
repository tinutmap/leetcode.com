# https://leetcode.com/problems/first-bad-version/

class Solution:
    def __init__(self, bad_version) -> None:
        self.bad_version = bad_version

    def isBadVersion(self, i):
        # bad_version = 4
        return i == self.bad_version

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        isBadVersion = self.isBadVersion  # add isBadVersion instance to local def namespace. Don't copy this line to leetcode IDE.

    # [1, 2, 3, 4, 5, 6, 7, 8]
    # bad_version = 7
    # n = 8
    #     l = 1
    #     r = 8
        # while
        #    mid = (1+8)// 2 = 4
        #    if isBadVersion(mid):
        #        r = mid - 1
        #    else:
        #        l = mid + 1

        #    if isBadVersion(4) # False
        #    else:
        #        l = 4 + 1 = 5

        #    mid = (5+8)// 2 = 6
        #    if isBadVersion(mid):
        #        r = mid - 1
        #    else:
        #        l = mid + 1

        #    if isBadVersion(6) # False
        #    else:
        #        l = 6 + 1 = 7

        #    mid = (7+8)// 2 = 7
        #    if isBadVersion(mid):
        #        r = mid - 1
        #    else:
        #        l = mid + 1

        #    if isBadVersion(6) # False
        #    else:
        #        l = 6 + 1 = 7

        # # Solution 1:
        # # Solution link
        # if isBadVersion(l) == isBadVersion(r):
        #     return l
        # else:  # meaning l is good, r is bad, thus first bad is in between
        #     while l+1 < r:
        #         mid = (l + r) // 2
        #         if isBadVersion(mid):
        #             r = mid
        #         else:
        #             l = mid

        #     return r

        # while 1 + 1 < 8:  # True
        #     mid = 4
        #     if isBadVersion(4):  # False
        #     else:
        #         l = 4

        # while 4+1 < 8  # True
        #     mid = 6
        #     if isBadVersion(6):  # False
        #     else:
        #         l = 6

        # while 6+1 < 8  # True
        #     mid = 7
        #     if isBadVersion(7):  # True
        #         r = 7

        # while 6 + 1 < 7  # False
        # return 7  # correct!

        # Solution 2: average performance
        # Solution link: https://leetcode.com/problems/first-bad-version/submissions/902978887/
        if n == 1:
            return 1

        l, r = 1, n
        while l < r:
            mid = l + (r-l)//2
            if isBadVersion(mid):
                r = mid-1
            else:
                l = mid+1
        return l if isBadVersion(l) else l+1

        # # Forum solution: a bit more orthodoxical
        # # Solution link: https://leetcode.com/problems/first-bad-version/solutions/71324/python-understand-easily-from-binary-search-idea/
        # i = 1
        # j=n
        # while i<j:
        #     k=(i+j)//2
        #     if isBadVersion(k):
        #         j=k
        #     else:
        #         i=k+1
        # return i
