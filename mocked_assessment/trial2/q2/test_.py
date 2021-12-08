from .code import Solution


def test_1():
    points = [[1, 3], [-2, 2]]
    k = 1
    result = [[-2, 2]]
    assert Solution().kClosest(points, k) == result


def test_2():
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    result1 = [[3, 3], [-2, 4]]
    result2 = [[-2, 4], [3, 3]]
    assert Solution().kClosest(
        points, k) == result1 or Solution().kClosest(points, k) == result2
