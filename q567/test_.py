from .code import Solution


def test_1():
    s1 = "ab"
    s2 = "eidbaooo"
    result = True
    assert Solution().checkInclusion(s1, s2) == result


def test_2():
    s1 = "ab"
    s2 = "eidboaoo"
    result = False
    assert Solution().checkInclusion(s1, s2) == result


def test_3():
    s1 = "d"
    s2 = "eidboaoo"
    result = True
    assert Solution().checkInclusion(s1, s2) == result


def test_4():
    s1 = "abooo"
    s2 = "eidboaoo"
    result = True
    assert Solution().checkInclusion(s1, s2) == result


def test_5():
    s1 = "abooi"
    s2 = "eidboaoo"
    result = False
    assert Solution().checkInclusion(s1, s2) == result


def test_6():
    s1 = "idbooa"
    s2 = "eidboaoo"
    result = True
    assert Solution().checkInclusion(s1, s2) == result


"""
"ab"
"eidbaooo"
"ab"
"eidboaoo"
"d"
"eidboaoo"
"abooo"
"eidboaoo"
"abooi"
"eidboaoo"
"idbooa"
"eidboaoo"
"""
