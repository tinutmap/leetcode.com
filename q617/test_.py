from .code import Solution, make_tree


def test_1():
    root1 = [1, 3, 2, 5]
    root2 = [2, 1, 3, None, 4, None, 7]
    result = [3, 4, 5, 5, 4, None, 7]
    assert Solution().mergeTrees(make_tree(root1), make_tree(root2)).to_list() == result


def test_2():
    root1 = [1]
    root2 = [1, 2]
    result = [2, 2]
    assert Solution().mergeTrees(make_tree(root1), make_tree(root2)).to_list() == result


"""
[1,3,2,5]
[2,1,3,null,4,null,7]
[1]
[1,2]
"""
