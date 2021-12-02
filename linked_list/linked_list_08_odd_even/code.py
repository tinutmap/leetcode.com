# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/

from typing import List, Optional
from ..base import ListNode, SinglyLinkedList


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Result https://leetcode.com/submissions/detail/595128349/?from=explore&item_id=1208
        '''
        try:
            odd_node = head
            even_node = first_even_node = odd_node.next
            cur_node = even_node.next
            i = 1
            while cur_node:
                if i % 2 == 1:  # odd
                    i = 0
                    odd_node.next = cur_node
                    odd_node = odd_node.next
                else:  # even
                    i = 1
                    even_node.next = cur_node
                    even_node = even_node.next
                cur_node = cur_node.next
            even_node.next = None
            odd_node.next = first_even_node
            return head
        except:
            return head

    def oddEvenList_local(self, head: Optional[SinglyLinkedList]) -> List:
        try:
            odd_node = head.head
            even_node = first_even_node = odd_node.next
            cur_node = even_node.next
            i = 1
            while cur_node:
                if i % 2 == 1:  # odd
                    i = 0
                    odd_node.next = cur_node
                    odd_node = odd_node.next
                else:  # even
                    i = 1
                    even_node.next = cur_node
                    even_node = even_node.next
                cur_node = cur_node.next
            even_node.next = None
            odd_node.next = first_even_node
            return head.head.to_list()
        except:
            if head.head:
                return head.head.to_list()
            else:
                return []

    '''
    Solution:
    # https://leetcode.com/problems/odd-even-linked-list/discuss/133345/With-detailed-explanation-or-Python
    '''
