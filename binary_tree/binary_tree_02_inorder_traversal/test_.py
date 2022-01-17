from .code import Solution
from binary_tree.base import make_tree


def test_1():
    root = [1, None, 2, 3]
    res = [1, 3, 2]
    assert Solution().inorderTraversal(make_tree(root)) == res


def test_2():
    root = []
    res = []
    assert Solution().inorderTraversal(make_tree(root)) == res


def test_3():
    root = [1]
    res = [1]
    assert Solution().inorderTraversal(make_tree(root)) == res


def test_4():
    root = ['A', 'B', 'D', None, 'C', 'E', 'F']
    res = ['B', 'C', 'A', 'E', 'D', 'F']
    assert Solution().inorderTraversal(make_tree(root)) == res


def test_5():
    root = ['F', 'B', 'G', 'A', 'D', None,
            'I', None, None, 'C', 'E', 'H', None]
    res = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', "I"]
    assert Solution().inorderTraversal(make_tree(root)) == res


"""
[1,null,2,3]
[]
[1]
[1, 2, 3, null, 4, 5, 6]
['F', 'B', 'G', 'A', 'D', null,'I', null, null, 'C', 'E', 'H', null]
"""
