# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from linked_list.base import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev_node = None
        while head.next:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node

        head.next = prev_node
        return head

    def reverseList_local(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.head
        if head is None:
            return ListNode(None)
        if head.next is None:
            return head

        prev_node = None
        while head.next:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node

        head.next = prev_node
        return head
