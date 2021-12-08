from .code import Solution


def test_1():
    s = "babad"
    result = ["bab", "aba"]
    assert Solution().longestPalindrome(s) in result


def test_2():
    s = "cbbd"
    result = ["bb"]
    assert Solution().longestPalindrome(s) in result


def test_3():
    s = "a"
    result = ["a"]
    assert Solution().longestPalindrome(s) in result


def test_4():
    s = "ac"
    result = ["a", "c"]
    assert Solution().longestPalindrome(s) in result


def test_5():
    s = "babadda"
    result = ["adda"]
    assert Solution().longestPalindrome(s) in result


'''
"babad"
"cbbd"
"a"
"ac"
"babadda"
'''
