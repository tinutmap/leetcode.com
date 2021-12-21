
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Definition for a Node.
from typing import List, Optional
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return f"{self.val}"

    def __bool__(self):
        if self.val == 0:
            return True
        else:
            return bool(self.val)

    def to_list(self):
        l = []
        if self:
            dq = deque([self])
            prev = None
            while dq:
                node = dq.popleft()
                if prev is None:
                    l.append(node.val)
                l.append(node.next.val if node.next else None)
                prev = node.next
                if node.left:
                    dq.append(node.left)
                    dq.append(node.right)
        return l


def make_tree(l: List = []):
    if l:
        root = Node(l[0])
        i = 1
        dq = deque([root])
        while i < len(l):
            node = dq.popleft()
            node.left = Node(l[i])
            dq.append(node.left)
            i += 1
            node.right = Node(l[i])
            dq.append(node.right)
            i += 1
        return root
    else:
        return Node(None)


class Solution:

    # # solution 1: passed
    # # https://leetcode.com/submissions/detail/602852445/
    # def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    #     if root:
    #         dq = deque([root])
    #         root.next = None
    #         level = 1
    #         is_bottom = False
    #         node = dq[0]
    #         while node.left:
    #             cur_node = None
    #             for i in range(2**level):
    #                 if not bool(i % 2):
    #                     node = dq.popleft()
    #                     if node.left:
    #                         dq.append(node.left)
    #                 elif node.right:
    #                     dq.append(node.right)

    #                 if cur_node is None:
    #                     cur_node = dq[-1]
    #                 else:
    #                     # print(i,dq)
    #                     cur_node.next = dq[-1]
    #                     cur_node = dq[-1]
    #             level += 1
    #             dq[-1].next = None
    #             node = dq[0]
    #         return root
    #     else:
    #         return Node(None)

    # solution 2: thanks to hint from forum solution
    # https://leetcode.com/submissions/detail/605084695/
    # https://leetcode.com/submissions/detail/605086738/

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root:
            cur = first = root
            cur.next = None
            while first.left:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                    cur = cur.next
                else:
                    cur.right.next = None
                    cur = first = first.left
        return root


"""
forum solution: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37465/Python-Solution-With-Explaintion
Key takeways:
    - using next pointer similar to linked list. No need to use deque.
"""
