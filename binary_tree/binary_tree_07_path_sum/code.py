# question link
# https://leetcode.com/problems/path-sum/
# https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/
from typing import Optional
from binary_tree.base import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # solution 1: brute-force recursive. worst cast O(n) TC, where n is total number of nodes. so-so performance.
        # solution link https://leetcode.com/submissions/detail/622776421/
        res = False

        def dfs(node, sum):
            nonlocal res
            if not res:
                # reaching leaf node
                if node.left is None and node.right is None:
                    res = (targetSum == sum+node.val)
                else:
                    if node.left:
                        dfs(node.left, sum+node.val)
                    if node.right:
                        dfs(node.right, sum+node.val)
        if root is not None:
            dfs(root, 0)

        return res
        # forum solution: DFS solution is similar to solution 1, except solution 1 has early termination `if not res`
        # using stack
        # solution link https://leetcode.com/problems/path-sum/discuss/36581/My-Python-iterative-DFS-solution
