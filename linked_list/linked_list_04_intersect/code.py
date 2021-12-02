# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/

from typing import List


class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return str(self.val)


'''
Failed Solution
class LinkedList:
    def __init__(self, l: List = [], result: ListNode = ListNode(0)) -> None:
        self.head = None
        self.len = 0
        if l:
            if l[0] == result.val:
                self.head = result
            else:
                self.head = ListNode(l[0])
            cur = self.head
            self.len += 1

            for i in range(1, len(l)):
                if l[i] == result.val:
                    node = result
                else:
                    node = ListNode(l[i])
                cur.next = node
                cur = node
                self.len += 1


class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     pass

    def getIntersectionNode_local(self, headA: LinkedList, headB: LinkedList) -> ListNode:
        if headA.len >= headB.len:
            for _ in range(headA.len - headB.len):
                headA.head = headA.head.next
            l = headA.len - _ - 1
        else:
            for _ in range(headB.len - headA.len):
                headB.head = headB.head.next
            l = headA.len
        cur_headA, cur_headB = headA, headB

        for _ in range(l):
            if cur_headA.head != cur_headB.head:
                cur_headA.head = cur_headA.head.next
                cur_headB.head = cur_headB.head.next
            else:
                return cur_headA.head

        return 0
'''

# Leetcode solutions:
# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/discuss/49838/5-line-python-solution
# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/discuss/49924/Python-AC-solution-with-clear-explanation


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            if a:
                a = a.next
            else:
                a = headB
            if b:
                b = b.next
            else:
                b = headA
        return a
