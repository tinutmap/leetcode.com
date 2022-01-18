from .code import Solution
from binary_tree.base import make_tree, to_list


def test_1():
    root = [4, 2, 7, 1, 3, 6, 9]
    res = [4, 7, 2, 9, 6, 3, 1]
    assert to_list(Solution().invertTree(make_tree(root))) == res


def test_2():
    root = [2, 1, 3]
    res = [2, 3, 1]
    assert to_list(Solution().invertTree(make_tree(root))) == res


def test_3():
    root = []
    res = []
    assert to_list(Solution().invertTree(make_tree(root))) == res


"""
[4,2,7,1,3,6,9]
[2,1,3]
[]
"""
