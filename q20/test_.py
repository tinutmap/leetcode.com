from .code import Solution


def test_1():
    s = "()"
    res = True
    assert Solution().isValid(s) == res


def test_2():
    s = "()[]{}"
    res = True
    assert Solution().isValid(s) == res


def test_3():
    s = "(]"
    res = False
    assert Solution().isValid(s) == res


def test_4():
    s = "([{}])"
    res = True
    assert Solution().isValid(s) == res


def test_5():
    s = "("
    res = False
    assert Solution().isValid(s) == res


def test_6():
    s = "]"
    res = False
    assert Solution().isValid(s) == res


def test_7():
    s = "(("
    res = False
    assert Solution().isValid(s) == res


def test_8():
    s = "))"
    res = False
    assert Solution().isValid(s) == res


"""
"()"
"()[]{}"
"(]"
"([{}])"
"("
"]"
"(("
"))"
"""
