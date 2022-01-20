# question link https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

from typing import Optional
from binary_tree.base import TreeNode


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # # solution 1: Good TC, so-so SC.
        # # solution link https://leetcode.com/problems/two-sum-iv-input-is-a-bst/submissions/
        # d = set()
        # res = False

        # def inorder(node):
        #     nonlocal res
        #     if node and not res:
        #         inorder(node.left)
        #         if k-node.val in d:
        #             res = True
        #         else:
        #             d.add(node.val)
        #         inorder(node.right)

        # inorder(root)
        # return res

        # forum solution: very neat solution, good use of BST. Expected solution in the interview
        # solution link https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/1420711/C%2B%2BJavaPython-3-solutions%3A-HashSet-Stack-Python-yield-Solutions-O(H)-space
        # better SC
        def pushLeft(st, root):
            while root:
                st.append(root)
                root = root.left

        def pushRight(st, root):
            while root:
                st.append(root)
                root = root.right

        def nextLeft(st):
            node = st.pop()
            pushLeft(st, node.right)
            return node.val

        def nextRight(st):
            node = st.pop()
            pushRight(st, node.left)
            return node.val

        stLeft, stRight = [], []
        pushLeft(stLeft, root)
        pushRight(stRight, root)

        left, right = nextLeft(stLeft), nextRight(stRight)
        while left < right:
            if left + right == k:
                return True
            if left + right < k:
                left = nextLeft(stLeft)
            else:
                right = nextRight(stRight)
        return False
