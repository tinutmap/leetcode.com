from .code import Solution
from binary_tree.base import make_tree


def test_1():
    root = [2, 1, 3]
    res = True
    assert Solution().isValidBST(make_tree(root)) == res


def test_2():
    root = [5, 1, 4, None, None, 3, 6]
    res = False
    assert Solution().isValidBST(make_tree(root)) == res


def test_3():
    root = [4, 1, 5, None, None, 3, 6]
    res = False
    assert Solution().isValidBST(make_tree(root)) == res


def test_4():
    root = [5, 3, 6, 1, 4]
    res = True
    assert Solution().isValidBST(make_tree(root)) == res


"""
[2,1,3]
[5,1,4,null,null,3,6]
[4,1,5,null,null,3,6]
[5, 3, 6, 1, 4]
"""
