from .code import Solution
from binary_tree.base import make_tree


def test_1():
    root = [1, None, 2, 3]
    res = [1, 2, 3]
    assert Solution().preorderTraversal(make_tree(root)) == res


def test_2():
    root = []
    res = []
    assert Solution().preorderTraversal(make_tree(root)) == res


def test_3():
    root = [1]
    res = [1]
    assert Solution().preorderTraversal(make_tree(root)) == res


def test_4():
    root = [1, 2, 3, None, 4, 5, 6]
    res = [1, 2, 4, 3, 5, 6]
    assert Solution().preorderTraversal(make_tree(root)) == res


"""
[1,None,2,3]
[]
[1]
[1, 2, 3, null, 4, 5, 6]
"""
