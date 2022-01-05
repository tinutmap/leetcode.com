# question link
class Solution:
    # # solution 1: brute-force using recursion:
    # # LTE
    # def climbStairs(self, n: int) -> int:
    #     res = 0

    #     def recurse(steps: int) -> int:
    #         nonlocal res
    #         if steps < n:
    #             for step in (1, 2):
    #                 recurse(steps + step)
    #         elif steps == n:
    #             res += 1
    #     recurse(0)
    #     return res

    # solution 2: step(n) = step(n-1) + step(n-2)
    # Fibonacci!
    # https://leetcode.com/submissions/detail/613739669/
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        minus_2, minus_1 = 1, 2
        for _ in range(3, n+1):
            res = minus_2 + minus_1
            minus_2, minus_1 = minus_1, res
        return res

    # # forum solution: just a bit more Pythonic
    # # https://leetcode.com/problems/climbing-stairs/discuss/25296/3-4-short-lines-in-every-language
    # def climbStairs(self, n):
    #     a = b = 1
    #     for _ in range(n):
    #         a, b = b, a + b
    #     return a
