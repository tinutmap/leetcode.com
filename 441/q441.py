class Solution:
    def arrangeCoins(self, n: int) -> int:
        delta = (1+8*n)
        upper_k = (-1 + delta**(1/2))/2
        return int(upper_k)


s = Solution()
print(s.arrangeCoins(9))
