from .code import Solution, to_list, make_tree


def test_1():
    root = [1, 2, 3, 4, 5, None, 7]
    res = [1, None, 2, 3, None, 4, 5, 7, None]
    assert to_list(Solution().connect(make_tree(root))) == res


def test_2():
    root = []
    res = []
    assert to_list(Solution().connect(make_tree(root))) == res


# test_3 does not work with def make_tree borrowed from q116
# def test_3():
#     root = [1, 2, None, 3, None, 4, None, 5]
#     res = []
#     assert to_list(Solution().connect(make_tree(root))) == res


"""
[1,2,3,4,5,null,7]
[]
[1,2,null,3,null,4,null,5]
"""
