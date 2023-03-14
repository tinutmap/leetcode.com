# https://leetcode.com/problems/flood-fill/
from typing import List


class Solution:
    # # solution 1: recursive
    # # https://leetcode.com/submissions/detail/601950203/
    # # https://leetcode.com/submissions/detail/602277592/
    # def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    #     if newColor != image[sr][sc]:
    #         m, n = len(image), len(image[0])
    #         self.recursive(image, sr, sc, newColor, m, n, image[sr][sc])
    #     return image

    # def recursive(self, image: List[List[int]], sr: int, sc: int, newColor: int, m: int, n: int, cur_color: int) -> List[List[int]]:
    #     dir_l = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    #     image[sr][sc] = newColor
    #     for dir in dir_l:
    #         # if sr+dir[0] >= 0 and sr+dir[0] < m \
    #         #     and sc+dir[1] >= 0 and sc+dir[1] < n \
    #         #         and image[sr+dir[0]][sc+dir[1]] == cur_color:
    #         if sr+dir[0] in range(m) and sc+dir[1] in range(n) \
    #                 and image[sr+dir[0]][sc+dir[1]] == cur_color:
    #             self.recursive(
    #                 image, sr+dir[0], sc+dir[1], newColor, m, n, cur_color)

    # solution 2: recursive. Average performance, bad memory. Revisit 4/13/2023 in 29:20
    # https://leetcode.com/problems/flood-fill/submissions/915077686/

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        old_color = image[sr][sc]

        def recurse(r, c):
            if (-1 < r < m) and (-1 < c < n) and (image[r][c] == old_color):
                image[r][c] = newColor
                for (i, j) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    recurse(r+i, c+j)

        if old_color != newColor:
            recurse(sr, sc)
        return image


"""
forum solution:
https://leetcode.com/problems/flood-fill/discuss/109604/Easy-Python-DFS-(no-need-for-visited)!!!
Key takeaways:
- use a<b<c is valid in Python
- use list comprehension seems pythonic: e.g. [traverse(row + x, col + y) for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]
- def in def for recursive.

"""
