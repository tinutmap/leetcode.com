# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val}"


def make_tree(l: List):
    if not l:
        return None
    root = TreeNode(l[0])
    dq = deque([root])
    i = 1
    try:
        while i < len(l):
            node = dq.popleft()
            if l[i] != None:
                left_node = TreeNode(l[i])
                node.left = left_node
                dq.append(left_node)
            i += 1

            if l[i] != None:
                right_node = TreeNode(l[i])
                node.right = right_node
                dq.append(right_node)
            i += 1
    except:
        pass
    return root
