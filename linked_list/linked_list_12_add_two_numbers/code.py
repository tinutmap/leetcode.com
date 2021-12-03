# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1228/
from typing import Optional
from ..base import ListNode, SinglyLinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    """
        # Solution 1: ugly and slow as F https://leetcode.com/submissions/detail/596124073/?from=explore&item_id=1228
        def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
           result = result_head = ListNode()
           carry_over = 0
           while l1 and l2:
               result.val = (l1.val + l2.val + carry_over) % 10
               carry_over = (l1.val + l2.val + carry_over) // 10

               l1 = l1.next
               l2 = l2.next
               if l1 and l2:
                   result.next = ListNode(None)
                   result = result.next

           rem_l = rem_l_head = (l1 or l2)
           if not rem_l:
               rem_l_head = None if carry_over == 0 else ListNode(carry_over)
           else:
               while carry_over != 0:
                   val = rem_l.val
                   rem_l.val = (val + carry_over) % 10
                   carry_over = (val + carry_over) // 10
                   if carry_over != 0:
                       if rem_l.next:
                           rem_l = rem_l.next
                       else:
                           rem_l.next = ListNode(0)
                           rem_l = rem_l.next
           if rem_l_head:
               result.next = rem_l_head

           return result_head

       def addTwoNumbers_local(self, l1: Optional[SinglyLinkedList], l2: Optional[SinglyLinkedList]) -> Optional[ListNode]:
           result = result_head = ListNode()
           carry_over = 0
           while l1.head and l2.head:
               result.val = (l1.head.val + l2.head.val + carry_over) % 10
               carry_over = (l1.head.val + l2.head.val + carry_over) // 10

               l1.head = l1.head.next
               l2.head = l2.head.next
               if l1.head and l2.head:
                   result.next = ListNode(None)
                   result = result.next

           rem_l = rem_l_head = (l1.head or l2.head)
           if not rem_l:
               rem_l_head = None if carry_over == 0 else ListNode(carry_over)
           else:
               while carry_over != 0:
                   val = rem_l.val
                   rem_l.val = (val + carry_over) % 10
                   carry_over = (val + carry_over) // 10
                   if carry_over != 0:
                       if rem_l.next:
                           rem_l = rem_l.next
                       else:
                           rem_l.next = ListNode(0)
                           rem_l = rem_l.next
           if rem_l_head:
               result.next = rem_l_head

           return result_head.to_list()
    """

    """ 
    # Solution 2: less spaghetti, inferior runtime, better memory than solution 1
    # https://leetcode.com/submissions/detail/596467268/?from=explore&item_id=1228
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_head = l1
        l2_head = l2
        if not l1_head or not l2_head:
            return l1_head.to_list() or l2_head.to_list()

        result = result_head = ListNode(0)
        carry_over = 0
        # dictate l1 to be the longer list
        while l1_head:
            result.next = ListNode(0)
            result = result.next
            result.val = (l1_head.val + l2_head.val + carry_over) % 10
            carry_over = (l1_head.val + l2_head.val + carry_over) // 10
            l1_head = l1_head.next
            l2_head = l2_head.next

            if l1_head is None:
                # swap l1_head and l2_head to make sure l1 longer
                l1_head, l2_head = l2_head, l1_head
            if l2_head is None:
                l2_head = ListNode(0)

        if carry_over == 1:
            result.next = ListNode(carry_over)
            result = result.next

        return result_head.next

    def addTwoNumbers_local(self, l1: Optional[SinglyLinkedList], l2: Optional[SinglyLinkedList]) -> Optional[ListNode]:
        l1_head = l1.head
        l2_head = l2.head
        if not l1_head or not l2_head:
            return l1_head.to_list() or l2_head.to_list()

        result = result_head = ListNode(0)
        carry_over = 0
        # dictate l1 to be the longer list
        while l1_head:
            result.next = ListNode(0)
            result = result.next
            result.val = (l1_head.val + l2_head.val + carry_over) % 10
            carry_over = (l1_head.val + l2_head.val + carry_over) // 10
            l1_head = l1_head.next
            l2_head = l2_head.next

            if l1_head is None:
                # swap l1_head and l2_head to make sure l1 longer
                l1_head, l2_head = l2_head, l1_head
            if l2_head is None:
                l2_head = ListNode(0)

        if carry_over == 1:
            result.next = ListNode(carry_over)
            result = result.next

        return result_head.next.to_list() 
    """

    # Solution 3: combined best of 1 and 2, less spaghetting code but still not great
    # https://leetcode.com/submissions/detail/596483570/?from=explore&item_id=1228

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = result = ListNode(0)
        carry_over = 0
        while l1 and l2:
            result.next = ListNode(0)
            result = result.next
            result.val = (l1.val + l2.val + carry_over) % 10
            carry_over = (l1.val + l2.val + carry_over) // 10
            l1 = l1.next
            l2 = l2.next
            # result.next = ListNode(0)
            # result = result.next

        # make sure l1 is longer if l1 or l2 still presents
        if l1 is None and l2:
            l1 = l2

        while carry_over == 1:
            if l1 is None:
                l1 = ListNode(0)
            result.next = ListNode(0)
            result = result.next
            result.val = (l1.val + carry_over) % 10
            carry_over = (l1.val + carry_over) // 10
            l1 = l1.next
            # result = result.next
        if l1:
            result.next = l1

        return result_head.next

    def addTwoNumbers_local(self, l1: Optional[SinglyLinkedList], l2: Optional[SinglyLinkedList]) -> Optional[ListNode]:
        result_head = result = ListNode(0)
        carry_over = 0
        while l1.head and l2.head:
            result.next = ListNode(0)
            result = result.next
            result.val = (l1.head.val + l2.head.val + carry_over) % 10
            carry_over = (l1.head.val + l2.head.val + carry_over) // 10
            l1.head = l1.head.next
            l2.head = l2.head.next
            # result.next = ListNode(0)
            # result = result.next

        # make sure l1 is longer if l1 or l2 still presents
        if l1.head is None and l2.head:
            l1.head = l2.head

        while carry_over == 1:
            if l1.head is None:
                l1.head = ListNode(0)
            result.next = ListNode(0)
            result = result.next
            result.val = (l1.head.val + carry_over) % 10
            carry_over = (l1.head.val + carry_over) // 10
            l1.head = l1.head.next
            # result = result.next
        if l1.head:
            result.next = l1.head

        return result_head.next.to_list()


""" 
Solutions: https://leetcode.com/problems/add-two-numbers/discuss/1016/Clear-python-code-straight-forward
Key takeaways:
- Use divmod()
- In a crunch, just let the loop run through using `while l1 or l2 or carry:`
- use dummy result head node = ListNode(0) then return `result.next` otherwise, it's mind burdening AF to decide when to loop result = result.next

"""
