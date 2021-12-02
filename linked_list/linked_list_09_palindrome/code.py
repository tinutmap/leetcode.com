from typing import Optional
from ..base import ListNode, SinglyLinkedList


class Solution:
    '''
    # Solution 1: Failed test 7
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        try:
            slow = head
            sum_slow = slow.val
            fast = slow.next
            sum_fast = slow.val + fast.val
        except:
            return True
        fast = fast.next
        odd = False
        while fast:
            slow = slow.next
            sum_slow += slow.val

            sum_fast += fast.val
            fast = fast.next
            if fast:
                sum_fast += fast.val
            else:
                odd = True
                break
            fast = fast.next

        if odd:
            sum_slow -= slow.val
            sum_fast -= slow.val

        if 2*sum_slow == sum_fast:
            return True
        else:
            return False

    def isPalindrome_local(self, head: Optional[SinglyLinkedList]) -> bool:
        try:
            slow = head.head
            sum_slow = slow.val
            fast = slow.next
            sum_fast = slow.val + fast.val
        except:
            return True
        fast = fast.next
        odd = False
        while fast:
            slow = slow.next
            sum_slow += slow.val

            sum_fast += fast.val
            fast = fast.next
            if fast:
                sum_fast += fast.val
            else:
                odd = True
                break
            fast = fast.next

        if odd:
            sum_slow -= slow.val
            sum_fast -= slow.val

        if 2*sum_slow == sum_fast:
            return True
        else:
            return False

# Solution 2: Failed test 9
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = slow.next
        if not fast:
            return True
        if not fast.next:
            return slow.val == fast.val
        odd = True
        while_run = False
        try:
            while fast.next and fast.next.next:
                while_run = True
                odd = not odd
                save_fast = fast
                # fast = fast.next
                # try:
                #     if fast.next and fast.next.next:
                fast = fast.next

                slow.next = None
                save_fast.next = slow
                slow = save_fast

                # else:
                #     break
                # except:
                #     break
                # fast = fast.next
        except:
            pass
        # compare slow and fast:
        if not while_run:
            slow.next = None
            fast = fast.next
        elif odd:
            slow = slow.next
        while slow:
            if slow.val == fast.val:
                slow = slow.next
                fast = fast.next
            else:
                return False
        return True

    def isPalindrome_local(self, head: Optional[SinglyLinkedList]) -> bool:
        slow = head.head
        fast = slow.next
        if not fast:
            return True
        if not fast.next:
            return slow.val == fast.val
        odd = True
        while_run = False
        try:
            while fast.next and fast.next.next:
                while_run = True
                odd = not odd
                save_fast = fast
                # fast = fast.next
                # try:
                #     if fast.next and fast.next.next:
                fast = fast.next

                slow.next = None
                save_fast.next = slow
                slow = save_fast

                # else:
                #     break
                # except:
                #     break
                # fast = fast.next
        except:
            pass
        # compare slow and fast:
        if not while_run:
            slow.next = None
            fast = fast.next
        elif odd:
            slow = slow.next
        while slow:
            if slow.val == fast.val:
                slow = slow.next
                fast = fast.next
            else:
                return False
        return True

    '''
    # Solution 3: Passed https://leetcode.com/submissions/detail/595601140/?from=explore&item_id=1209

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = slow.next
        if not fast:
            return True
        reversed_slow = ListNode(slow.val)
        next_slow = slow.next
        while fast:
            fast = fast.next
            if fast:
                if fast.next:
                    slow = next_slow
                    next_slow = slow.next
                    slow.next = reversed_slow
                    reversed_slow = slow

                else:
                    next_slow = next_slow.next
                    break
            else:
                break
            fast = fast.next

        while reversed_slow:
            if reversed_slow.val == next_slow.val:
                reversed_slow = reversed_slow.next
                next_slow = next_slow.next
            else:
                return False
        return True

    def isPalindrome_local(self, head: Optional[SinglyLinkedList]) -> bool:
        slow = head.head
        fast = slow.next
        if not fast:
            return True
        reversed_slow = ListNode(slow.val)
        next_slow = slow.next
        while fast:
            fast = fast.next
            if fast:
                if fast.next:
                    slow = next_slow
                    next_slow = slow.next
                    slow.next = reversed_slow
                    reversed_slow = slow

                else:
                    next_slow = next_slow.next
                    break
            else:
                break
            fast = fast.next

        while reversed_slow:
            if reversed_slow.val == next_slow.val:
                reversed_slow = reversed_slow.next
                next_slow = next_slow.next
            else:
                return False
        return True
