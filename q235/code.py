# question link https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
from binary_tree.base import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # solution 1:
        # solution link
        # https://leetcode.com/submissions/detail/624020146/
        # https://leetcode.com/submissions/detail/624021279/
        if p.val > q.val:
            p, q = q, p
        while True:
            if root.val > q.val:
                root = root.left
            elif root.val < p.val:
                root = root.right
            else:
                break
        return root

        # # solution 2: revisit 2/22/2023 failed.
        # # solution link
        # if q.val < p.val:
        #     p, q = q, p
        # stack = [root]
        # node = root

        # # search p first
        # while node.val != p.val:
        #     node = stack.pop()
        #     if p.val > node.val:
        #         stack.append(node.right)
        #     elif p.val == node.val:
        #         stack.append(node)
        #     else:
        #         stack.append(node.left)

        # while True:
        #     node = stack.pop()

        #     def is_q_in_this_node(node):
        #         if node.val == q.val:
        #             return True
        #         if node.left and is_q_in_this_node(node.left):
        #             return True
        #         if node.right and is_q_in_this_node(node.right):
        #             return True
        #     if is_q_in_this_node(node):
        #         return node

        # forum solution: same idea, recursive is also another method
        # the `root = (root.left, root.right)[p.val > root.val]` is badass but sacrifice readability
        # solution link https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/discuss/64963/3-lines-with-O(1)-space-1-Liners-Alternatives
