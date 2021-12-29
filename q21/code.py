# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from linked_list.base import ListNode
import math


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1, list2 = list1.head, list2.head
        if not list1 or not list2:
            return list1 or list2 or None
        if list1.val > list2.val:
            list1, list2 = list2, list1
        list1_head = list1
        while list1 and list2:
            list1_next = list1.next.val if list1.next else math.inf
            if list1.val <= list2.val <= list1_next:
                list2_node = list2
                list2 = list2.next
                list2_node.next = list1.next
                list1.next = list2_node
                list1 = list2_node
            else:
                list1 = list1.next

        if list2:
            list1.next = list2
        return list1_head if list1_head else None

    def mergeTwoLists_local(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1, list2 = list1.head, list2.head
        if not list1 or not list2:
            return list1 or list2 or ListNode(None)

        if list1.val > list2.val:
            list1, list2 = list2, list1
        list1_head = list1
        while list1 and list2:
            list1_next = list1.next.val if list1.next else math.inf
            if list1.val <= list2.val <= list1_next:
                list2_node = list2
                list2 = list2.next
                list2_node.next = list1.next
                list1.next = list2_node
                list1 = list2_node
            else:
                list1 = list1.next

        if list2:
            list1.next = list2
        return list1_head if list1_head else ListNode(None)
