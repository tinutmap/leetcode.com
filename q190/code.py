# https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        # solution 1: inferior using string processing
        # https://leetcode.com/submissions/detail/614989662/
        b = bin(n)[2:]
        padding = ['0' for _ in range(len(b), 32)]
        b = ''.join(padding) + b
        return int(b[-1::-1], 2)

        # # forum solution: brilliant utilization of bit shifting
        # # https://leetcode.com/problems/reverse-bits/discuss/54748/AC-Python-44-ms-solution-bit-manipulation
        # res = 0
        # for _ in range(32):
        #     res = (res << 1) | (n & 1)
        #     n >>= 1
        # return res

        # forum solution with O(logn) time complexity:
        # https://leetcode.com/problems/reverse-bits/discuss/54741/O(1)-bit-operation-C%2B%2B-solution-(8ms)
