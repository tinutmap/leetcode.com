from typing import List
from collections import deque


class Solution:
    # solution 1: accepted. https://leetcode.com/submissions/detail/608876952/
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque([])
        m, n = len(grid), len(grid[0])
        good_orange = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    good_orange += 1
                elif grid[i][j] == 2:
                    dq.append((i, j, 0))
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        count = 0
        while dq:
            r, c, count = dq.popleft()
            for d in directions:
                r_ = r + d[0]
                c_ = c + d[1]
                if 0 <= r_ < m and 0 <= c_ < n and grid[r_][c_] == 1:
                    grid[r_][c_] = 2
                    dq.append((r_, c_, count+1))
                    good_orange -= 1

        return -1 if good_orange > 0 else count
