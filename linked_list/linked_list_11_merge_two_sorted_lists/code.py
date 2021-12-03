from typing import Optional
from ..base import ListNode, SinglyLinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1: https://leetcode.com/submissions/detail/596084179/?from=explore&item_id=1227


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy head with min value to dictacte the of l2 > l1 -> add l2 to l1
        dummy_l1_head = ListNode(-101)
        dummy_l1_head.next = list1
        list1 = dummy_l1_head

        l1_cur = list1
        # l2_cur = list2

        #
        while l1_cur:
            if list2:
                try:
                    l2_cur = list2
                    if l2_cur.val >= l1_cur.val and l2_cur.val < l1_cur.next.val:
                        # remove l2 head and add to l1
                        list2 = list2.next
                        l2_cur.next = l1_cur.next
                        l1_cur.next = l2_cur
                    l1_cur = l1_cur.next
                except:  # except raise when l1_cur.next is None
                    if list2:
                        l1_cur.next = list2
                    break
            else:
                break

        list1 = list1.next  # remove dummy head
        return None if list1 == None else list1

    def mergeTwoLists_local(self, list1: Optional[SinglyLinkedList], list2: Optional[SinglyLinkedList]) -> Optional[SinglyLinkedList]:
        # create dummy head with min value to dictacte the of l2.head > l1.head -> add l2 to l1
        dummy_l1_head = ListNode(-101)
        dummy_l1_head.next = list1.head
        list1.head = dummy_l1_head

        l1_cur = list1.head

        while l1_cur:
            if list2.head:
                try:
                    l2_cur = list2.head
                    if l2_cur.val >= l1_cur.val and l2_cur.val < l1_cur.next.val:
                        # remove l2 head and add to l1
                        list2.head = list2.head.next
                        l2_cur.next = l1_cur.next
                        l1_cur.next = l2_cur
                    l1_cur = l1_cur.next
                except:  # except raise when l1_cur.next is None
                    if list2.head:
                        l1_cur.next = list2.head
                    break
            else:
                break

        list1.head = list1.head.next  # remove dummy head
        return [] if list1.head == None else list1.head.to_list()


'''
Solution:
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1227/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).

'''
