from .code import Solution


def test_1():
    s = "a1b2"
    res = ["a1b2", "a1B2", "A1b2", "A1B2"]
    assert Solution().letterCasePermutation(s).sort() == res.sort()


def test_2():
    s = "3z4"
    res = ["3z4", "3Z4"]
    assert Solution().letterCasePermutation(s).sort() == res.sort()


def test_3():
    s = "123"
    res = ["123"]
    assert Solution().letterCasePermutation(s).sort() == res.sort()


"""
"a1b2"
"3z4"
"123"
"""
