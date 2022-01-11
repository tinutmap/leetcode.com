# question link https://leetcode.com/problems/pascals-triangle/
from typing import List


class Solution:
    # # solution 1: inferior
    # # https://leetcode.com/submissions/detail/617797515/
    # def generate(self, numRows: int) -> List[List[int]]:
    #     res = [[1], [1, 1]]
    #     if numRows == 1:
    #         return [res[0]]

    #     for i in range(2, numRows):
    #         res_ = []
    #         for j in range(i-1):
    #             res_.append(res[i-1][j]+res[i-1][j+1])
    #         res.append([1] + res_ + [1])
    #     # res_ = [res[i-1][j]+res[i-1][j+1]
    #     #         for i in range(2, numRows) for j in range(i-1)
    #     #        ]
    #     # res.append(res_)
    #     # res.append([1] +
    #     #            [res[i-1][j]+res[i-1][j+1]
    #     #             for i in range(2, numRows) for j in range(i-1)
    #     #             ]
    #     #            + [1])
    #     return res

    # solution 2: mirror res_ using slicing so only need to calculate half a row each row
    # still inferior, and worse than solution 1, probably due to modulo's expensive
    # https://leetcode.com/submissions/detail/617800753/
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]
        if numRows == 1:
            return [res[0]]

        for i in range(2, numRows):
            res_ = []
            for j in range((i)//2):
                res_.append(res[i-1][j]+res[i-1][j+1])
            # if i % 2 == 0:
            #     res_ = res_ + res_[-2::-1]
            # else:
            res_ = [1]+res_ + res_[-1-(i % 2 == 0)::-1]+[1]
            res.append(res_)
        return res

    # forum solution:
    # next row = ([previous row] + [0]) + ([0] + [previous row])
    # https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map.
    # or pre-generate the matrix and just do the job in a brilliant way
    # https://leetcode.com/problems/pascals-triangle/discuss/38277/Simple-Python-4-lines
