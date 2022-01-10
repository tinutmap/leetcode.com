from .code import Solution


def test_1():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    res = [1, 2, 2, 3, 5, 6]
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == res


def test_2():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    res = [1]
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == res


def test_3():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    res = [1]
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == res


def test_4():
    nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    m = 6
    nums2 = [1, 2, 2]
    n = 3
    res = [-1, 0, 0, 1, 2, 2, 3, 3, 3]
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == res


def test_5():
    nums1 = [-1, -1, 0, 0, 0, 0]
    m = 4
    nums2 = [-1, 0]
    n = 2
    res = [-1, -1, -1, 0, 0, 0]
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == res


"""
[1,2,3,0,0,0]
3
[2,5,6]
3
[1]
1
[]
0
[0]
0
[1]
1
[-1, 0, 0, 3, 3, 3, 0, 0, 0]
6
[1, 2, 2]
3
[-1,-1,0,0,0,0]
4
[-1,0]
2
[-1, -1, 0, 0, 0, 0]
4
[-1, 0]
2
"""
