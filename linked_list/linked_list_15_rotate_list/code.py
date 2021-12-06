# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ..base import ListNode, SinglyLinkedList
from typing import Optional


class Solution:
    # Solution 1: accepted https://leetcode.com/submissions/detail/597892251/?from=explore&item_id=1295
    '''
1 -> 2 -> 3

k = 1
3 -> 2 -> 1

k = 2
2 -> 3 -> 1

k = 3
1 -> 2 -> 3

- new_k = k % 3, 3 is length of list (n)
-> run entire list to find n. Also at tail, connect tail to head.
- run n - new_k - 1 to find prev_node that precedes new_head to be returned.
- Disconnect prev_node and new_head and return new_head

'''

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # if not cur_node.next:
        #     return head
        cur_node = head
        n = 1
        while cur_node.next:
            cur_node = cur_node.next
            n += 1

        k = k % n
        if k == 0:
            return head

        cur_node.next = head
        cur_node = head
        for _ in range(n-k-1):
            cur_node = cur_node.next

        result_node = cur_node.next
        cur_node.next = None
        return result_node

    def rotateRight_local(self, head: Optional[SinglyLinkedList], k: int) -> Optional[SinglyLinkedList]:
        cur_node = head.head
        if not cur_node:
            return []
        if not cur_node.next:
            return cur_node.to_list()

        n = 1
        while cur_node.next:
            cur_node = cur_node.next
            n += 1

        k = k % n
        if k == 0:
            return head.head.to_list()

        cur_node.next = head.head

        cur_node = head.head
        for _ in range(n-k-1):
            cur_node = cur_node.next

        result_node = cur_node.next
        cur_node.next = None
        return result_node.to_list()
