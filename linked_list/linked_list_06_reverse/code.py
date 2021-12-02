# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1205/
# Definition for singly-linked list.
from typing import Optional
from ..base import SinglyLinkedList, ListNode


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        else:
            cur_node = head
            prev_node = None

            while cur_node.next:
                next_node = cur_node.next
                cur_node.next = prev_node
                prev_node = cur_node
                cur_node = next_node
            cur_node.next = prev_node

            return cur_node

    def reverseList_local(self, head: Optional[SinglyLinkedList]) -> Optional[ListNode]:
        if not head.head:
            return []
        else:
            cur_node = head.head
            prev_node = None

            while cur_node.next:
                next_node = cur_node.next
                cur_node.next = prev_node
                prev_node = cur_node
                cur_node = next_node
            cur_node.next = prev_node

            return cur_node.to_list()


'''
Solution:
# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1205/discuss/1449712/Easy-C++JavaPythonJavaScript-Explained+Animated
'''
