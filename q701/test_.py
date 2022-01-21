from .code import Solution
from binary_tree.base import make_tree, to_list


def test_1():
    root = [5, 2, 7, 1, 4]
    val = 3
    res = [4, 2, 7, 1, 3, 5]
    assert to_list(Solution().insertIntoBST(make_tree(root), val)) == res


def test_2():
    root = [4, 2, 7, 1, 3]
    val = 5
    res = [4, 2, 7, 1, 3, 5]
    assert to_list(Solution().insertIntoBST(make_tree(root), val)) == res


def test_3():
    root = [40, 20, 60, 10, 30, 50, 70]
    val = 25
    res = [40, 25, 60, 20, 30, 50, 70, 10]
    assert to_list(Solution().insertIntoBST(make_tree(root), val)) == res


def test_4():
    root = [4, 2, 7, 1, 3, None, None, None, None, None, None]
    val = 5
    res = [4, 2, 7, 1, 3, 5]
    assert to_list(Solution().insertIntoBST(make_tree(root), val)) == res


def test_5():
    root = [61, 46, 66, 43, None, None, None, 39, None, None, None]
    val = 88
    res = [61, 43, 88, 39, 46, 66]
    assert to_list(Solution().insertIntoBST(make_tree(root), val)) == res


"""
[5, 2, 7, 1, 4]
3
[4,2,7,1,3]
5
[40,20,60,10,30,50,70]
25
[4,2,7,1,3,null,null,null,null,null,null]
5
[61,46,66,43,null,null,null,39,null,null,null]
88
"""
