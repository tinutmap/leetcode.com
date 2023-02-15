# question link https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

from collections import deque
from typing import List

# Definition for a Node.


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


def to_list(root):
    l = []
    if root:
        dq = deque([root])
        prev = None
        while dq:
            node = dq.popleft()
            if prev is None:
                l.append(node.val)
            l.append(node.next.val if node.next else None)
            prev = node.next
            if node.left:
                dq.append(node.left)
            if node.right:
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
    def connect(self, root: 'Node') -> 'Node':
        # solution 1: so-so TC, not so good SC
        # solution link https://leetcode.com/submissions/detail/626898825/
        if root is None:
            return
        queue = deque([[root]])
        while queue:
            nodes = queue.popleft()
            # add dummy node at index 0 to kickstart the first chain of link
            next_level_nodes = deque([Node()])
            for node in nodes:
                for child_node in (node.left, node.right):
                    if child_node is not None and child_node.val is not None:
                        next_level_nodes[-1].next = child_node
                        next_level_nodes.append(child_node)
            # remove the dummy node at index 0
            next_level_nodes.popleft()
            if next_level_nodes:
                queue.append(next_level_nodes)

        return root

    # # solution 2: failed solution at test case 4
    # # solution link
    # if root is None:
    #     return
    # queue = deque([root, None])
    # prev_node = None
    # while queue:
    #     node = queue.popleft()
    #     # prev_node = node.left or node.right or None
    #     if node is None:
    #         prev_node = None
    #         if len(queue) > 1:
    #             queue.append(None)
    #     else:
    #         for child_node in (node.left, node.right):
    #             if child_node is not None and child_node.val is not None:
    #                 if prev_node is not None:
    #                     prev_node.next = child_node
    #                 prev_node = child_node
    #                 queue.append(child_node)
    # return root

    # # forum solution: O(1) SC, use one dummy as preceding node at each parent level
    # # and tail node as child node. node is the current parent node
    # # solution link https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/37824/AC-Python-O(1)-space-solution-12-lines-and-easy-to-understand
    # def connect(self, node):
    #     tail = dummy = Node(0)
    #     while node:
    #         tail.next = node.left
    #         if tail.next:
    #             tail = tail.next
    #         tail.next = node.right
    #         if tail.next:
    #             tail = tail.next
    #         node = node.next
    #         if not node:
    #             tail = dummy
    #             node = dummy.next
