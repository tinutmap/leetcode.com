# question link
# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/
# https://leetcode.com/problems/binary-tree-postorder-traversal/


from typing import List, Optional
from binary_tree.base import TreeNode
from collections import deque


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # solution 1: recursive.
        # # solution link https://leetcode.com/submissions/detail/621856690/
        # res = []

        # def recurse(node):
        #     if node:
        #         recurse(node.left)
        #         recurse(node.right)
        #         res.append(node.val)
        # recurse(root)
        # return res

        # solution 2: iterative.
        # solution link https://leetcode.com/submissions/detail/621894261/
        res = deque([])
        stack = [root]
        while stack:
            node = stack.pop()

            if node:
                res.appendleft(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return list(res)
        # # forum solution: other consideration is Morris Traversal Time
        # # solution link https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45628/Morris-Traversal-Time-O(n)-Space-O(1)-inorder-preorder-postorder
