# question link https://leetcode.com/problems/search-a-2d-matrix/
from typing import List
import math


class Solution:
    # solution 1: inferior
    # solution link https://leetcode.com/submissions/detail/618591553/
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(l: List) -> int:
            start, end = 0, len(l)-1
            while start < end:
                mid = start + (end - start) // 2
                if l[start] == target or l[end] == target or l[mid] == target:
                    return 1
                elif l[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return - 1

        first_col = [-math.inf]+list(list(zip(*matrix))[0])+[math.inf]
        # binary search first column to find right row:
        start, end = 0, len(first_col)-1
        if target < matrix[0][start] or target > matrix[end-2][len(matrix[0])-1]:
            return False

        while True:
            mid = start + (end - start) // 2
            if first_col[mid] < target < first_col[mid+1]:
                break
            if first_col[start] == target or first_col[end] == target or first_col[mid] == target:
                return True
            elif first_col[mid] < target:
                start = mid+1
            else:
                end = mid-1

        return binary_search(matrix[mid-1]) == 1
    # forum solution:
    # flatten the list to 1D and binary search
    # https://leetcode.com/problems/search-a-2d-matrix/discuss/896821/Python-Simple-binary-search-explained
    # using library:
    # https://leetcode.com/problems/search-a-2d-matrix/discuss/26248/6-12-lines-O(log(m)-%2B-log(n))-myself%2Blibrary
