# question link
# https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/535/
# https://leetcode.com/problems/maximum-depth-of-binary-tree/


from typing import Optional
from binary_tree.base import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # solution 1: bottom up. Why is it so inferior in performance?
        # solution link https://leetcode.com/submissions/detail/622018388/
        def dfs(node, depth):
            if node:
                return max(dfs(node.left, depth), dfs(node.right, depth))+1
            return 0
        return dfs(root, 1)

        # # solution 2: top down. inferior as well
        # # solution link https://leetcode.com/submissions/detail/622026314/
        # res = 0

        # def dfs(node, depth):
        #     nonlocal res
        #     if node:
        #         dfs(node.left, depth+1)
        #         dfs(node.right, depth+1)
        #     res = max(res, depth-1)
        # dfs(root, 1)
        # return res

        # forum solution: also feasible using BFS. no difference in performance
        # link https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/34345/Python-BFS-solution
