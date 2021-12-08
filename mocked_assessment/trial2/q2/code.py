from typing import List


class Solution:
    # solution 1: https://leetcode.com/submissions/detail/598539902/
    # good performance but may missing other more efficient methods, see solution takeaway:
    # def dist(l: list):
    #     return l[0]**2 + l[1]**2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        return points[0:k]


"""
Some solutions worth checking:
- using heappq library:
    - https://leetcode.com/problems/k-closest-points-to-origin/discuss/217999/JavaC%2B%2BPython-O(N)
    - https://leetcode.com/problems/k-closest-points-to-origin/discuss/294389/Easy-to-read-Python-min-heap-solution-(-beat-99-python-solutions-)
- using scipy.spatial to implement kd-tree https://leetcode.com/problems/k-closest-points-to-origin/discuss/576025/Python-3-lines-kNN-search-using-kd-tree-(for-large-number-of-queries)
- official solution: https://leetcode.com/problems/k-closest-points-to-origin/solution/

"""
