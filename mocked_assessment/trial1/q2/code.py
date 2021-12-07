class Solution:
    # Solution 1: passed but naive
    def hammingWeight(self, n: int) -> int:
        b = bin(n)
        count = 0
        for i in range(len(b)-1, -1, -1):
            if b[i] == '1':
                count += 1
            elif b[i] == 'b':
                break
        return count


"""
Solution: https://leetcode.com/problems/number-of-1-bits/discuss/1044775/Python-n-and-(n-1)-trick-%2B-even-faster-explained
Key takeaways:
- Cheating way, convert to string and use str.count('1')
- Bitwise operation: everytime using n & (n-1), the rightmost '1' will be removed. Then count number of times until n=0
"""
