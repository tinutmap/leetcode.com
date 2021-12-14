from typing import List
# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        range_l = []
        n_locations = n+1
        for i in range(n_locations):
            if ranges[i] != 0:
                range_l.append([max(i-ranges[i], 0),
                                min(i+ranges[i], n)])
                # range_l.append([i-ranges[i], i+ranges[i]])
            else:
                range_l.append([None, None])
        print(range_l)

    # prep: 2D matrix
    # tap_matrix = [[None for _ in range(n_locations)]
    #               for _ in range(n_locations)]

    # for i in range(n_locations):
    #     try:
    #         for j in range(range_l[i][0], range_l[i][1]+1):
    #             tap_matrix[i][j] = 1
    #     except:
    #         pass
    # print(tap_matrix)

    # min_tap_l = [0 for _ in range(n_locations)]
    # for i in range_l:
    #     if i[0] == 0:
    #         min_tap_l[0] = 1
    #         break
    #     else:
    #         return -1
    # for i in range(1, min_tap_l):
    #     min_tap_l[i] = min_tap_l[i-1] + min()

    # solution 1: failed test_4
    # min_tap_l = []
    # for i in range(n_locations):
    #     for j in range(n_locations):
    #         isFound = False
    #         try:
    #             if range_l[j][0] <= i and i <= range_l[j][1]:
    #                 isFound = True
    #                 if j < i:
    #                     # min_tap_l = min_tap_l
    #                     pass
    #                 else:
    #                     min_tap_l += 1
    #                 break
    #         except:
    #             pass
    #     if not isFound:
    #         return -1
    # return min_tap_l

    # solution 2: pass with inferior performance
    # https: // leetcode.com/submissions/detail/599976405/
        min_tap_l = []
        for i in range(n_locations):
            isFound = False
            for j in min_tap_l:
                try:
                    if range_l[j][0] <= i and i <= range_l[j][1]:
                        isFound = True
                        break
                except:
                    pass
            if not isFound:
                best_j = None
                for j in range(n_locations):
                    try:
                        if i == 0:
                            i_temp = 1
                        else:
                            i_temp = i
                        if range_l[j][0] <= i_temp-1 and i_temp <= range_l[j][1] and j not in min_tap_l:
                            if best_j is None or range_l[best_j][1] < range_l[j][1]:
                                best_j = j
                    except:
                        pass
                if best_j is None:
                    return -1
                for k in min_tap_l:
                    if range_l[k][0] >= range_l[best_j][0] and range_l[k][1] <= range_l[best_j][1]:
                        min_tap_l.pop(k)
                min_tap_l.append(best_j)

        return len(min_tap_l)

    # forum solution:
    # https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/712660/DP-pattern-to-solve-3-similar-problems
    # https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/484235/JavaC%2B%2BPython-Similar-to-LC1024

    """     
    def minTaps(self, n, A):
        dp = [0] + [n + 2] * n
        for i, x in enumerate(A):
            for j in range(max(i - x + 1, 0), min(i + x, n) + 1):
                dp[j] = min(dp[j], dp[max(0, i - x)] + 1)
        return dp[n] if dp[n] < n + 2 else -1
    """
