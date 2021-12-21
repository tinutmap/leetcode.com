from .code import Solution, make_tree


def test_1():
    root = [1, 2, 3, 4, 5, 6, 7]
    result = [1, None, 2, 3,  None, 4, 5, 6, 7,  None]
    assert Solution().connect(make_tree(root)).to_list() == result


def test_2():
    root = [0]
    result = [0, None]
    assert Solution().connect(make_tree(root)).to_list() == result


def test_3():
    root = []
    result = []
    assert Solution().connect(make_tree(root)).to_list() == result


"""
[1, 2, 3, 4, 5, 6, 7]
[0]
[]
"""
