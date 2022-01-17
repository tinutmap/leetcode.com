from .code import Solution
from binary_tree.base import make_tree


def test_1():
    root = [3, 9, 20, None, None, 15, 7]
    res = 3
    assert Solution().maxDepth(make_tree(root)) == res


def test_2():
    root = []
    res = 0
    assert Solution().maxDepth(make_tree(root)) == res


def test_3():
    root = [1, None, 2]
    res = 2
    assert Solution().maxDepth(make_tree(root)) == res


def test_4():
    root = [1, 2, 4, None, 3, 5, 6]
    res = 3
    assert Solution().maxDepth(make_tree(root)) == res


def test_5():
    root = [6, 2, 7, 1, 4, None,
            9, None, None, 3, 5, 8, None]
    res = 4
    assert Solution().maxDepth(make_tree(root)) == res


"""
[3,9,20,null,null,15,7]
[]
[1,null,2]
[1, 2, 4, null, 3, 5, 6]
[6, 2, 7, 1, 4, null, 9, null, null, 3, 5, 8, null]
"""
