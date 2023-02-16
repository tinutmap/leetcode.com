from .code import Solution


def test_1():
    s = "abc"
    t = "ahbgdc"
    res = True
    assert Solution().isSubsequence(s, t) == res


def test_2():
    s = "axc"
    t = "ahbgdc"
    res = False
    assert Solution().isSubsequence(s, t) == res


def test_3():
    s = "abc"
    t = ""
    res = False
    assert Solution().isSubsequence(s, t) == res


def test_4():
    s = ""
    t = "abc"
    res = True
    assert Solution().isSubsequence(s, t) == res


def test_5():
    s = "aaaaaa"
    t = "bbaaaa"
    res = False
    assert Solution().isSubsequence(s, t) == res


"""
"""
