from q3 import lengthOfLongestSubstring as f


def test_1():
    assert f("tmmzuxt") == 5


def test_2():
    assert f('abcabcbb') == 3


def test_3():
    assert f('bbbbb') == 1


def test_4():
    assert f('pwwkew') == 3


def test_5():
    assert f('') == 0


def test_6():
    assert f(' ') == 1


"""
"tmmzuxt"
"abcabcbb"
"bbbbb"
"pwwkew"
""
" "
"""
