from typing import List
import math


class Solution:
    """
    # Solution 1: Failed test 6 due to stack over flown. DFS using recursive is a bad decision here.
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def recurse(i, j, step, min_step):
            try:
                if step > min_step or i >= m or i < 0 or j >= n or j < 0:
                    return min_step
                elif res[i][j] is not None:
                    return res[i][j] + 1
                elif mat[i][j] == 0:
                    res[i][j] = 0
                    return 1
                else:

                    # min_step = min(recurse(i-1, j, step+1, min_step), min_step)
                    # visited[i-1][j] = 1
                    # min_step = min(recurse(i, j-1, step+1, min_step), min_step)
                    # visited[i][j-1] = 1
                    min_step = min(recurse(i+1, j, step+1, min_step), min_step)
                    # visited[i+1][j] = 1
                    min_step = min(recurse(i, j+1, step+1, min_step), min_step)
                    # visited[i][j+1] = 1
                    return min_step + 1
            except:
                pass
        m = len(mat)
        n = len(mat[0])
        res = [[None for j in range(n)]for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    min_step = 10**4 * 2
                    # visited = [[0 for j in range(n)]for i in range(m)]
                    # visited[i][j] = 1
                    # min_step = min(recurse(i-1, j, 0, min_step), min_step)
                    # min_step = min(recurse(i, j-1, 0, min_step), min_step)
                    if i > 0:
                        min_step = min(res[i-1][j]+1, min_step)
                    if j > 0:
                        min_step = min(res[i][j-1]+1, min_step)
                    min_step = min(recurse(i+1, j, 0, min_step), min_step)
                    min_step = min(recurse(i, j+1, 0, min_step), min_step)
                    res[i][j] = min_step
        return res
    """

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[None for j in range(n)]for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    top = res[i-1][j]+1 if i > 0 else math.inf
                    left = res[i][j-1]+1 if j > 0 else math.inf
                    res[i][j] = min(top, left)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                bottom = res[i+1][j]+1 if i < m-1 else math.inf
                right = res[i][j+1]+1 if j < n-1 else math.inf
                res[i][j] = min(res[i][j], bottom, right)

        return res


"""
Community solutions:
https://leetcode.com/problems/01-matrix/discuss/1369741/C%2B%2BJavaPython-BFS-DP-solutions-with-Picture-Clean-and-Concise-O(1)-Space
"""
