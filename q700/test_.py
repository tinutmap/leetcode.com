from .code import Solution
from binary_tree.base import make_tree, to_list


def test_1():
    root = [4, 2, 7, 1, 3]
    val = 2
    res = [2, 1, 3]
    assert to_list(Solution().searchBST(make_tree(root), val)) == res


def test_2():
    root = [1, 2, 3]
    val = 5
    res = []
    assert to_list(Solution().searchBST(make_tree(root), val)) == res


"""
"""
