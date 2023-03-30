from .code import Solution


def test_1():
    strs = ["flower", "flow", "flight"]
    res = 'fl'
    assert Solution().longestCommonPrefix(strs) == res


def test_2():
    strs = ["dog", "racecar", "car"]
    res = ''
    assert Solution().longestCommonPrefix(strs) == res


def test_3():
    strs = [""]
    res = ''
    assert Solution().longestCommonPrefix(strs) == res


def test_4():
    strs = ["a"]
    res = 'a'
    assert Solution().longestCommonPrefix(strs) == res


"""
["flower","flow","flight"]
["dog","racecar","car"]
[""]
["a"]
"""
