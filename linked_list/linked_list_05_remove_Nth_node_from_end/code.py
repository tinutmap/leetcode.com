# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/
from typing import List, Optional
from ..base import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#     def __repr__(self) -> str:
#         return str(self.val)


class LinkedList:
    def __init__(self, l: List = [],):
        self.head = None
        if l:
            self.head = ListNode(l[0])
            cur = self.head
            for i in range(1, len(l)):
                node = ListNode(l[i])
                cur.next = node
                cur = node


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        l = 0
        deleted_node, prev_node = head, head
        while cur.next:
            cur = cur.next
            l += 1
            if l >= n:
                deleted_node = deleted_node.next
            if l > n:
                prev_node = prev_node.next
        if l-n == -1:
            head = deleted_node.next
        elif l-n > -1:
            prev_node.next = deleted_node.next
        return head

    def removeNthFromEnd_local(self, head: Optional[LinkedList], n: int) -> Optional[ListNode]:
        cur = head.head
        l = 0
        deleted_node, prev_node = head.head, head.head
        while cur.next:
            cur = cur.next
            l += 1
            if l >= n:
                deleted_node = deleted_node.next
            if l > n:
                prev_node = prev_node.next

        if l-n == -1:
            head.head = deleted_node.next
        elif l-n > -1:
            prev_node.next = deleted_node.next

        try:
            return head.head.to_list()
        except:
            return []


'''
key takeaway:
- loop from head n times to shift the linked list where from that index the cur can start moving
- can loop with loop or recursive
- solutions
  https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/discuss/8802/3-short-Python-solutions
  https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/discuss/1164542/JS-Python-Java-C++-or-Easy-Two-Pointer-Solution-w-Explanation
'''
