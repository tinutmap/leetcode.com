# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional
from linked_list.base import SinglyLinkedList, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# SinglyLinkList = base.SinglyLinkedList


class Solution:
    # Passed: https://leetcode.com/submissions/detail/597961252/
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        if not slow.next:
            return slow

        fast = slow.next
        if not fast.next:
            return fast

        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break

        return slow

    def middleNode_local(self, head: Optional[SinglyLinkedList]) -> Optional[SinglyLinkedList]:
        slow = head.head
        if not slow.next:
            return slow.to_list()

        fast = slow.next
        if not fast.next:
            return fast.to_list()

        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break

        return slow.to_list()

# Solution: # https://leetcode.com/problems/middle-of-the-linked-list/discuss/154619/C%2B%2BJavaPython-Slow-and-Fast-Pointers
