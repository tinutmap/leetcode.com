from .code import Solution
from binary_tree.base import make_tree


def test_1():
    root = [5, 3, 6, 2, 4, None, 7]
    k = 9
    res = True
    assert Solution().findTarget(make_tree(root), k) == res


def test_2():
    root = [5, 3, 6, 2, 4, None, 7]
    k = 28
    res = False
    assert Solution().findTarget(make_tree(root), k) == res


"""
[5,3,6,2,4,null,7]
9
[5,3,6,2,4,null,7]
28
"""
