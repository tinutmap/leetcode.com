from .code import Solution


def test_1():
    s = "3[a2[c]d2[e]]f"
    res = "accdeeaccdeeaccdeef"
    assert Solution().decodeString(s) == res


def test_2():
    s = "3[a]2[bc]"
    res = "aaabcbc"
    assert Solution().decodeString(s) == res


def test_3():
    s = "3[a2[c]]"
    res = "accaccacc"
    assert Solution().decodeString(s) == res


def test_4():
    s = "2[abc]3[cd]ef"
    res = "abcabccdcdcdef"
    assert Solution().decodeString(s) == res


def test_5():
    s = "10[abc]"
    res = "abcabcabcabcabcabcabcabcabcabc"
    assert Solution().decodeString(s) == res


"""
"3[a2[c]d2[e]]f"
"3[a]2[bc]"
"3[a2[c]]"
"2[abc]3[cd]ef"
"10[abc]"
"""
