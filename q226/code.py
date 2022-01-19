# question link https://leetcode.com/problems/invert-binary-tree/
from typing import Optional
from binary_tree.base import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # solution 1: not so good performance?!
        # solution link https://leetcode.com/submissions/detail/622796418/
        def dfs(node):
            node.left, node.right = node.right, node.left
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        if root:
            dfs(root)

        return root

        # forum solution: more concise code from God! a bit better TC
        # solution link https://leetcode.com/problems/invert-binary-tree/discuss/62714/3-4-lines-Python
        # https://leetcode.com/submissions/detail/622798025/
