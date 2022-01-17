# question link
# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/
# https://leetcode.com/problems/binary-tree-inorder-traversal/


from typing import List, Optional
from binary_tree.base import TreeNode
from collections import deque


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # solution 1: recursive.
        # solution link https://leetcode.com/submissions/detail/621829927/
        res = []

        def recurse(node):
            if node:
                recurse(node.left)
                res.append(node.val)
                recurse(node.right)
        recurse(root)
        return res

        # # forum solution:
        # # solution link https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31381/Python-recursive-and-iterative-solutions.

        # res, stack = [], []
        # while True:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     if not stack:
        #         return res
        #     node = stack.pop()
        #     res.append(node.val)
        #     root = node.right
