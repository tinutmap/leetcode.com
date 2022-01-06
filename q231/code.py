# https://leetcode.com/problems/power-of-two/
class Solution:
    # # solution 1: inferior time o(n), good memory
    # # https://leetcode.com/submissions/detail/614463808/
    # def isPowerOfTwo(self, n: int) -> bool:
    #     b = bin(n)[2:]
    #     try:
    #         return int(b[-1::-1]) == 1
    #     except:
    #         return False

    # # solution 2: good time O(n), bad memory
    # # https://leetcode.com/submissions/detail/614471014/
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while bin(n)[-1] == '0':
            n = n >> 1
        return n == 1

    # # solution 3: forum solution
    # # https://leetcode.com/problems/power-of-two/discuss/1638707/PythonC%2B%2BJava-Detailly-Explain-Why-n-and-n-1-Works-oror-1-Line-oror-100-Faster-oror-Easy
    # # summary of forum solutions
    # # https://leetcode.com/problems/power-of-two/discuss/1638961/C%2B%2BPython-Simple-Solutions-w-Explanation-or-All-Possible-Solutions-Explained
    # # great O() space complexity discussion
    # # https://leetcode.com/problems/power-of-two/discuss/1638961/C++Python-Simple-Solutions-w-Explanation-or-All-Possible-Solutions-Explained/1187488
    # def isPowerOfTwo(self, n: int) -> bool:
    #     return n != 0 and (n & n-1) == 0
