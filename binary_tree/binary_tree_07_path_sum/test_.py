from .code import Solution
from binary_tree.base import make_tree


def test_1():
    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    targetSum = 22
    res = True
    assert Solution().hasPathSum(make_tree(root), targetSum) == res


def test_2():
    root = [1, 2, 3]
    targetSum = 5
    res = False
    assert Solution().hasPathSum(make_tree(root), targetSum) == res


def test_3():
    root = []
    targetSum = 0
    res = False
    assert Solution().hasPathSum(make_tree(root), targetSum) == res


"""
[5,4,8,11,null,13,4,7,2,null,null,null,1]
22
[1,2,3]
5
[]
0
"""
