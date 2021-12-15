# https://leetcode.com/problems/max-area-of-island/
from typing import List


class Solution:
    """
    # solution 1: passed but inferior performance
    # https://leetcode.com/submissions/detail/602314976/
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = [[0 for _ in range(columns)] for __ in range(rows)]
        max_a = 0

        def find_island_a(r, c):
            dir_l = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            # dir_l = [[1, 0], [0, 1]]
            visited[r][c] = 1
            a = 1
            for dir in dir_l:
                if 0 <= r+dir[0] < rows and 0 <= c+dir[1] < columns \
                    and not visited[r+dir[0]][c+dir[1]] \
                        and grid[r+dir[0]][c+dir[1]]:
                    a += find_island_a(r+dir[0], c+dir[1])
            return a
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] and not visited[i][j]:
                    # a = find_island_a(i, j)
                    max_a = max(max_a, find_island_a(i, j))
                visited[i][j] = 1
        return max_a
    """

    """
    # solution 2: improved upon solution 1, still inferior
    # https://leetcode.com/submissions/detail/602317167/
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = [[0 for _ in range(columns)] for __ in range(rows)]
        max_a = 0

        def find_island_a(r, c):
            dir_l = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            visited[r][c] = 1
            a = 1
            for dir in dir_l:
                _r = r+dir[0]
                _c = c+dir[1]
                if _r in range(rows) and _c in range(columns) \
                    and not visited[_r][_c] \
                        and grid[_r][_c]:
                    a += find_island_a(_r, _c)
            return a
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] and not visited[i][j]:
                    # a = find_island_a(i, j)
                    max_a = max(max_a, find_island_a(i, j))
                visited[i][j] = 1
        return max_a
    """

    # solution 3: based on forum solution,
    # no need to use visited_array, instead modify grid[r][c] =0
    # no need to use dir_l array for directions
    # https://leetcode.com/submissions/detail/602320352/
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        max_a = 0

        def find_island_a(r, c):
            if r in range(rows) and c in range(columns) and grid[r][c]:
                grid[r][c] = 0
                return 1 + find_island_a(r-1, c) + find_island_a(r, c-1) + \
                    find_island_a(r+1, c) + find_island_a(r, c+1)
            else:
                return 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]:
                    max_a = max(max_a, find_island_a(i, j))
        return max_a


"""
forum solution: https://leetcode.com/problems/max-area-of-island/discuss/108541/easy-python

"""
