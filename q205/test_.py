from .code import Solution


def test_1():
    s = "egg"
    t = "add"
    res = True
    assert Solution().isIsomorphic(s, t) == res


def test_2():
    s = "foo"
    t = "bar"
    res = False
    assert Solution().isIsomorphic(s, t) == res


def test_3():
    s = "paper"
    t = "title"
    res = True
    assert Solution().isIsomorphic(s, t) == res


def test_4():
    s = "badc"
    t = "baba"
    res = False
    assert Solution().isIsomorphic(s, t) == res


"""
"""
