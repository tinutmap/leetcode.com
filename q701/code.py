# question link https://leetcode.com/problems/insert-into-a-binary-search-tree/

import math
from typing import List, Optional
from binary_tree.base import TreeNode


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # solution 1: inorder traverse tree to list and add val in right position.
        # Then convert list back to BST. Inferior performance
        # solution link https://leetcode.com/submissions/detail/624093016/

        found = False
        l = []

        def inorder(node):
            nonlocal found  # , prev_node
            if node:
                inorder(node.left)
                if node.val > val and not found:
                    l.append(val)
                    found = True
                l.append(node.val)
                inorder(node.right)

        inorder(root)
        if not found:
            l.append(val)

        # reconstruct BST:
        def bst(l: List):
            if l:
                mid = len(l)//2
                return TreeNode(val=l[mid], left=bst(l[0:mid]), right=bst(l[mid+1::]))
            else:
                return None
        return bst(l)

        # # forum solution:
        # # https://leetcode.com/problems/insert-into-a-binary-search-tree/discuss/1683942/Well-Detailed-Explaination-Java-C%2B%2B-Python-oror-Easy-for-mind-to-Accept-it
        # if root is None:
        #     return TreeNode(val)
        # if root.val > val:
        #     root.left = self.insertIntoBST(root.left, val)
        # else:
        #     root.right = self.insertIntoBST(root.right, val)
        # return root
