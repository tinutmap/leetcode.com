from .code import Solution


def test_1():
    s = "anagram"
    t = "nagaram"
    res = True
    assert Solution().isAnagram(s, t) == res


def test_2():
    s = "rat"
    t = "car"
    res = False
    assert Solution().isAnagram(s, t) == res


def test_3():
    s = "abb"
    t = "aba"
    res = False
    assert Solution().isAnagram(s, t) == res


"""
"""
