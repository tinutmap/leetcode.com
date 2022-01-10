from .code import Solution


def test_1():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    res = [2, 2]
    sol = Solution().intersect(nums1, nums2)
    sol.sort()
    assert sol == res


def test_2():
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    res = [4, 9]
    sol = Solution().intersect(nums1, nums2)
    sol.sort()
    assert sol == res


"""

"""
