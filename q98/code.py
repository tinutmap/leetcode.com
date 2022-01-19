# question link https://leetcode.com/problems/validate-binary-search-tree/
import math
from typing import Optional
from binary_tree.base import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # # solution 1: wrong solution. Need to do inorder traversal
        # # solution link
        # res = True

        # def dfs(node):
        #     nonlocal res
        #     if res:
        #         if node.left == node.right == None:
        #             pass
        #         elif node.left is None or node.right is None:
        #             res = False
        #         else:
        #             res = (node.left.val < node.val < node.right.val)
        #             dfs(node.left)
        #             dfs(node.right)
        # dfs(root)
        # return res

        # # solution 2: OK, not so good SC
        # # solution link: https://leetcode.com/submissions/detail/623478753/

        res = True
        prev_node = -math.inf

        def inorder(node):
            nonlocal res, prev_node
            if res and node:
                inorder(node.left)
                if node.val > prev_node:
                    prev_node = node.val
                else:
                    res = False
                inorder(node.right)
        inorder(root)
        return res

        # forum solution: similar inorder traversal. better performance
        # solution link https://leetcode.com/problems/validate-binary-search-tree/discuss/32178/Clean-Python-Solution
