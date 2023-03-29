# question link https://leetcode.com/problems/where-will-the-ball-fall/?envType=study-plan&id=level-2
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # solution 1: OK solution, feel great to catch the edge case at `col+1 == n or grid[row][col+1] == -1` that col+1 can be out of range and throws error
        # OK runtime and memory. Time 35 mins
        # solution link https://leetcode.com/problems/where-will-the-ball-fall/submissions/924463307/?envType=study-plan&id=level-2

        def drop(col):
            row = 0
            while row < m:
                if grid[row][col] == 1 and (col+1 == n or grid[row][col+1] == -1):
                    return -1
                if grid[row][col] == -1 and (col == 0 or grid[row][col-1] == 1):
                    return -1
                col += grid[row][col]
                row += 1
            return col

        m, n = len(grid), len(grid[0])
        re = []

        for i in range(n):
            re.append(drop(i))

        return re

        # forum solution: neater logic and great using map()
        # solution link https://leetcode.com/problems/where-will-the-ball-fall/solutions/988576/java-c-python-solution-with-explanation/
