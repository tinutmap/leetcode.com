# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/

# Definition for singly-linked list.


from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return str(self.val)


class Head:
    def __init__(self, l: List = [], pos=-1) -> None:
        if l:
            self.head = ListNode(l[0])
            cur = self.head
            if pos == -1:
                pos_node = None
            else:
                pos_node = self.head
            for i in range(1, len(l)):
                node = ListNode(l[i])
                if i == pos:
                    pos_node = node
                cur.next = node
                cur = node

            self.tail = cur
            self.tail.next = pos_node


class Solution:
    '''
    # solution 1
    def detectCycle(self, head: ListNode) -> ListNode:
    try:
        result = head
        turtle = head
        hare = head.next
        while hare != turtle:
            turtle = turtle.next
            hare = hare.next.next

        node_in_loop = turtle

        while turtle != result:
            turtle = turtle.next
            while node_in_loop != turtle:
                if turtle == result:
                    return result
                turtle = turtle.next
            result = result.next
        return result

    except:
        return None
    '''
    # solution 2:
    # https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare
    # https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/discuss/44783/Share-my-python-solution-with-detailed-explanation

    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            result = head
            turtle = head
            hare = head.next
            while hare != turtle:
                turtle = turtle.next
                hare = hare.next.next

            # node_in_loop = turtle
            turtle = turtle.next
            while turtle != result:
                # turtle = turtle.next
                # while node_in_loop != turtle:
                # if turtle == result:
                #     return result
                turtle = turtle.next
                result = result.next
            return result

        except:
            return None

    def detectCycle_local(self, head: ListNode) -> ListNode:
        '''
        This function is compatible with local setup and test
        '''
        try:
            result = head.head
            turtle = head.head
            hare = head.head.next
            while hare != turtle:
                turtle = turtle.next
                hare = hare.next.next

            # node_in_loop = turtle
            turtle = turtle.next
            while turtle != result:
                # turtle = turtle.next
                # while node_in_loop != turtle:
                # if turtle == result:
                #     return result
                turtle = turtle.next
                result = result.next
            return result

        except:
            return None


# head = Head([3, 2, 0, -4], 1)
# print(Solution().detectCycle_local(head))
