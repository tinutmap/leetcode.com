# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/

# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return str(self.val)


# credit https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/discuss/44494/Except-ionally-fast-Python


# LBYL: Look Before You Leap https://docs.python.org/3/glossary.html#term-LBYL
# EAFP: Easier to Ask for Forgiveness than Permission https://docs.python.org/3/glossary.html#term-EAFP

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            turle = head
            hare = head.next
            while turle != hare:
                turle = turle.next
                hare = hare.next.next
            return True
        except:
            return False


a = [3, 2, 0, -4]
b = Solution().hasCycle(a)
print(b)
