from n_rary_tree.base import make_tree
from .code import Solution


def test_1():
    root = [1, None, 3, 2, 4, None, 5, 6]
    root = make_tree(root)
    res = [1, 3, 5, 6, 2, 4]

    assert Solution().preorder(root) == res


def test_2():
    root = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None,
            9, 10, None, None, 11, None, 12, None, 13, None, None, 14]
    root = make_tree(root)
    res = [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]

    assert Solution().preorder(root) == res


"""
"""
