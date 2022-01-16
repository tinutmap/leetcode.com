# question link https://leetcode.com/problems/remove-duplicates-from-sorted-list/
from typing import Optional
from linked_list.base import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # solution 1: not so good performance
        # solution link https://leetcode.com/submissions/detail/619839370/
        if not head:
            return None
        res = first_head = head

        while head.next is not None:
            head = head.next
            if head.val != first_head.val:
                first_head.next = head
                first_head = head
        first_head.next = head.next
        return res

    def deleteDuplicates_local(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = res = first_head = head.head
        if not head:
            return ListNode(None)

        while head.next is not None:
            head = head.next
            if head.val != first_head.val:
                first_head.next = head
                first_head = head
        first_head.next = head.next
        return res

        # forum solution: better readability but same performance https://leetcode.com/submissions/detail/619880305/
        # solution link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/discuss/28621/Simple-iterative-Python-6-lines-60-ms
