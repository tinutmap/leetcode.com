# question link https://leetcode.com/problems/fibonacci-number/?envType=study-plan&id=level-1
class Solution:
    def fib(self, n: int) -> int:

        # solution 1: superior solution. time 8:05
        # solution link https://leetcode.com/problems/fibonacci-number/submissions/915694996/?envType=study-plan&id=level-1

        if n < 2:
            return n

        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a+b

        return a+b

        # forum solution: some more interesting approach
        # solution link https://leetcode.com/problems/fibonacci-number/solutions/308688/6-python-solutions/
