from q1489 import findCriticalAndPseudoCriticalEdges as f


def test_f():
    assert f('abcabcbb') == 3
    assert f('bbbbb') == 1
    assert f('pwwkew') == 3
    assert f('') == 0
    assert f(' ') == 1
