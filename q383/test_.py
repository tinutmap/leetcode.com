from .code import Solution


def test_1():
    ransomNote = "a"
    magazine = "b"
    res = False
    assert Solution().canConstruct(ransomNote, magazine) == res


def test_2():
    ransomNote = "aa"
    magazine = "ab"
    res = False
    assert Solution().canConstruct(ransomNote, magazine) == res


def test_3():
    ransomNote = "aa"
    magazine = "aab"
    res = True
    assert Solution().canConstruct(ransomNote, magazine) == res


"""
"a"
"b"
"aa"
"ab"
"aa"
"aab"
"""
