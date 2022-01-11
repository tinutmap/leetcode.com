# https://leetcode.com/problems/reshape-the-matrix/
from typing import List


class Solution:
    # # solution 1: inferior time complexity. superior space complexity
    # # https://leetcode.com/submissions/detail/617734172/
    # def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    #     r_mat, c_mat = len(mat), len(mat[0])
    #     if r_mat * c_mat != r*c:
    #         return mat
    #     res = [[None for _ in range(c)] for __ in range(r)]
    #     for i in range(len(mat)):
    #         for j in range(len(mat[0])):
    #             r_ = (i*c_mat + j) // c
    #             c_ = (i*c_mat + j) % c
    #             res[r_][c_] = mat[i][j]
    #     return res

    # solution 2: flatten mat to 1D and using slicing
    # https://leetcode.com/submissions/detail/617746242/
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        r_mat, c_mat = len(mat), len(mat[0])
        if r_mat * c_mat != r*c:
            return mat
        res = [[None for _ in range(c)] for __ in range(r)]
        # flatten mat to 1D
        flat_mat = []
        for i in range(r_mat):
            flat_mat += mat[i]
        res = []
        for i in range(r):
            res.append(flat_mat[i*c:(i+1)*c])
        return res

    # forum solution:
    # using numpy! or list comprehension and one loop to run (r*c) times and using div and mod
    # https://leetcode.com/problems/reshape-the-matrix/discuss/102500/Python-Solutions
