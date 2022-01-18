from .code import Solution
from binary_tree.base import make_tree


def test_1():
    root = root = [1, 2, 2, 3, 4, 4, 3]
    res = True
    assert Solution().isSymmetric(make_tree(root)) == res


def test_2():
    root = [1, 2, 2, None, 3, None, 3]
    res = False
    assert Solution().isSymmetric(make_tree(root)) == res


def test_3():
    root = [1]
    res = True
    assert Solution().isSymmetric(make_tree(root)) == res


def test_4():
    root = [1, 2, None]
    res = False
    assert Solution().isSymmetric(make_tree(root)) == res


def test_5():
    root = [1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5]
    res = True
    assert Solution().isSymmetric(make_tree(root)) == res


def test_6():
    root = [1, 2, None, 5]
    res = False
    assert Solution().isSymmetric(make_tree(root)) == res


def test_7():
    root = [2, 97, 97, None, 47, 80, None, -7, None, None, -7]
    res = False
    assert Solution().isSymmetric(make_tree(root)) == res


"""
[1,2,2,3,4,4,3]
[1,2,2,null,3,null,3]
[1]
[1,2,null]
[1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5]
[1, 2, null, 5]
[2, 97, 97, null, 47, 80, null, -7, null, null, -7]
"""
