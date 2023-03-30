# question link https://leetcode.com/problems/spiral-matrix/?envType=study-plan&id=level-2
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # solution 1: bad performance but works for 1st trial.
        # solution link https://leetcode.com/problems/spiral-matrix/submissions/924532445/?envType=study-plan&id=level-2
        m, n = len(matrix), len(matrix[0])
        done = 101

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0

        re = []

        i, j = 0, 0
        while len(re) < m*n:
            re.append(matrix[i][j])
            matrix[i][j] = done
            i += dirs[direction][0]
            j += dirs[direction][1]

            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] == done:
                i -= dirs[direction][0]
                j -= dirs[direction][1]
                direction = (direction+1) % 4
                i += dirs[direction][0]
                j += dirs[direction][1]

        return re

        # forum solution: great one-liner with constantly rotate the matrix.
        # solution link https://leetcode.com/problems/spiral-matrix/solutions/20571/1-liner-in-python-ruby/
