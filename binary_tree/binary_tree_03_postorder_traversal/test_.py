from .code import Solution
from binary_tree.base import make_tree


def test_1():
    root = [1, None, 2, 3]
    res = [3, 2, 1]
    assert Solution().postorderTraversal(make_tree(root)) == res


def test_2():
    root = []
    res = []
    assert Solution().postorderTraversal(make_tree(root)) == res


def test_3():
    root = [1]
    res = [1]
    assert Solution().postorderTraversal(make_tree(root)) == res


def test_4():
    root = [1, 2, 4, None, 3, 5, 6]
    res = [3, 2, 5, 6, 4, 1]
    assert Solution().postorderTraversal(make_tree(root)) == res


def test_5():
    root = [6, 2, 7, 1, 4, None,
            9, None, None, 3, 5, 8, None]
    res = [1, 3, 5, 4, 2, 8, 9, 7, 6]
    assert Solution().postorderTraversal(make_tree(root)) == res


"""
[1,null,2,3]
[]
[1]
[1, 2, 3, null, 4, 5, 6]
[6, 2, 7, 1, 4, null, 9, null, null, 3, 5, 8, null]
"""
