# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/

from typing import Optional
from ..base import SinglyLinkedList, ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # if not head:  # edge case empty list
        #     return None
        # else:
        try:  # this try/except will also catch edge case of empty list above
            # edge case: removed node at head
            while head.val == val:
                head = head.next
        except:
            return None

        cur_node = head
        prev_node = None
        while cur_node:
            if cur_node.val == val:
                prev_node.next = cur_node.next
            else:
                prev_node = cur_node
            cur_node = cur_node.next

        return head

    def removeElements_local(self, head: Optional[SinglyLinkedList], val: int):
        if not head.head:  # edge case empty list
            return []
        else:
            try:
                # edge case: removed node at head
                while head.head.val == val:
                    head.head = head.head.next
            except:
                return []

            cur_node = head.head
            prev_node = None
            while cur_node:
                if cur_node.val == val:
                    prev_node.next = cur_node.next
                else:
                    prev_node = cur_node
                cur_node = cur_node.next

            return head.head.to_list()
