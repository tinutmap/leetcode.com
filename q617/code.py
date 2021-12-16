# https://leetcode.com/problems/merge-two-binary-trees/
# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val}"

    def __bool__(self):
        return bool(self.val)

    def to_list(self):
        l = []
        if self:
            dq = deque([self])
            while dq:
                node = dq.popleft()
                if node:
                    l.append(node.val)
                    if node.left or node.right:
                        dq.append(node.left)
                        dq.append(node.right)
                else:
                    l.append(None)
            while l[-1] is None:
                l.pop()
        return l


def make_tree(l: List = []):
    if l:
        root = TreeNode(l[0])
        dq = deque([(root, 0, 0)])
        i = 0
        while dq:
            node, index, adjust = dq.popleft()
            index += adjust
            if index+2**i < len(l):
                node.left = TreeNode(l[index+2**i])
                dq.append((node.left, index+2**i, 0))
            if index+2**i+1 < len(l):
                node.right = TreeNode(l[index+2**i+1])
                dq.append((node.right, index+2**i+1, -1))
            i += 1

    return root or None


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        else:
            return root1 or root2
