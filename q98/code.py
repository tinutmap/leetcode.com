# question link https://leetcode.com/problems/validate-binary-search-tree/
import math
import collections
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

        # # # solution 2: OK, not so good SC
        # # # solution link: https://leetcode.com/submissions/detail/623478753/

        # res = True
        # prev_node = -math.inf

        # def inorder(node):
        #     nonlocal res, prev_node
        #     if res and node:
        #         inorder(node.left)
        #         if node.val > prev_node:
        #             prev_node = node.val
        #         else:
        #             res = False
        #         inorder(node.right)
        # inorder(root)
        # return res

        # # solution 3: a bit better than solution 2 by breaking recursion stacks by throwing/catching errors but still inferior
        # # solution link: https://leetcode.com/problems/validate-binary-search-tree/submissions/903097913/?envType=study-plan&id=level-1
        last = -math.inf

        def recurse(node):
            nonlocal last
            if node.left:
                recurse(node.left)
            if last < node.val:
                last = node.val
            else:
                raise Exception()
            if node.right:
                recurse(node.right)
        try:
            recurse(root)
            return True
        except:
            return False

        # forum solution: similar inorder traversal. better performance
        # solution link https://leetcode.com/problems/validate-binary-search-tree/discuss/32178/Clean-Python-Solution
