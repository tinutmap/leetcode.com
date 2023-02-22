from .code import Solution
from binary_tree.base import make_tree, TreeNode


def test_1():
    root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p = 2
    q = 8
    res = 6
    assert Solution().lowestCommonAncestor(make_tree(root),
                                           TreeNode(p), TreeNode(q)).val == res


def test_2():
    root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p = 2
    q = 4
    res = 2
    assert Solution().lowestCommonAncestor(make_tree(root),
                                           TreeNode(p), TreeNode(q)).val == res


def test_3():
    root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p = 3
    q = 5
    res = 4
    assert Solution().lowestCommonAncestor(make_tree(root),
                                           TreeNode(p), TreeNode(q)).val == res


def test_4():
    root = [2, 1]
    p = 2
    q = 1
    res = 2
    assert Solution().lowestCommonAncestor(make_tree(root),
                                           TreeNode(p), TreeNode(q)).val == res


def test_5():
    root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p = 3
    q = 9
    res = 6
    assert Solution().lowestCommonAncestor(make_tree(root),
                                           TreeNode(p), TreeNode(q)).val == res


"""
[6,2,8,0,4,7,9,null,null,3,5]
2
8
[6,2,8,0,4,7,9,null,null,3,5]
2
4
[2,1]
2
1
[6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]
3
5
[6,2,8,0,4,7,9,null,null,3,5]
3
9
"""
