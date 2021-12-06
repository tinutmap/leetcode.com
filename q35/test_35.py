from q35 import searchInsert


def test_1():
    assert searchInsert([1, 3, 5, 6], target=5) == 2


def test_2():
    assert searchInsert([1, 3, 5, 6], target=2) == 1


def test_3():
    assert searchInsert([1, 3, 5, 6], target=7) == 4


def test_4():
    assert searchInsert([1, 3, 5, 6], target=0) == 0


def test_5():
    assert searchInsert([1], target=0) == 0
