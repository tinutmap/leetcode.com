# question link https://leetcode.com/problems/valid-sudoku/
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # solution 1: inferior, really!
        # https://leetcode.com/submissions/detail/618456856/
        d_column = {k: set() for k in range(9)}
        d_sub_box = {(i, j): set() for i in range(3) for j in range(3)}

        for i in range(9):
            s = set()
            for j in range(9):
                e = board[i][j]
                if e.isdigit():
                    # test row
                    if e in s:
                        return False
                    else:
                        s.add(e)
                    # test column
                    if e in d_column[j]:
                        return False
                    else:
                        d_column[j].add(e)
                    # test 3x3
                    r_sub, c_sub = i // 3, j//3
                    if e in d_sub_box[(r_sub, c_sub)]:
                        return False
                    else:
                        d_sub_box[(r_sub, c_sub)].add(e)
        return True
        # forum solution:
        # more readable code, takeaway:  using zip
        # https://leetcode.com/problems/valid-sudoku/discuss/15451/A-readable-Python-solution
        # goddamn-it solution with few lines, takeaway: using enumarate
        # https://leetcode.com/problems/valid-sudoku/discuss/15460/1-7-lines-Python-4-solutions
