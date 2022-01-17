# question link
# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
# https://leetcode.com/problems/binary-tree-preorder-traversal/


from typing import List, Optional
from binary_tree.base import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # solution 1: recursion
        # # solution link https://leetcode.com/submissions/detail/621786667/
        # res = []

        # def recurse(node):
        #     if node:
        #         res.append(node.val)
        #         if node.left:
        #             recurse(node.left)
        #         if node.right:
        #             recurse(node.right)
        # recurse(root)
        # return res

        # solution 2: iteration
        # solution link https://leetcode.com/submissions/detail/621798409/
        res = []
        dq = [root]
        if root:
            while dq:
                node = dq.pop()
                res.append(node.val)
                if node.right:
                    dq.append(node.right)
                if node.left:
                    dq.append(node.left)

        return res

        # forum solution: only need if node at every node, more optimal than extra `if node.left` and `if node.right`
        # solution link https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/45290/Python-solutions-(recursively-and-iteratively).

        # recursion
        # res = []
        # def recurse(node):
        #     if node:
        #         res.append(node.val)
        #         recurse(node.left)
        #         recurse(node.right)
        # recurse(root)
        # return res

        # iterative
        # res = []
        # dq = [root]
        # if root:
        #     while dq:
        #         node = dq.pop()
        #         if node:
        #             res.append(node.val)
        #             dq.append(node.right)
        #             dq.append(node.left)

        # return res
