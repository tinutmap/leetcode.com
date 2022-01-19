# question link https://leetcode.com/problems/search-in-a-binary-search-tree/
from typing import Optional
from binary_tree.base import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # solution 1: iterative. Seems no matter how concise solution is, the performance is inferior.
        # Probably leetcode is more crowded these days
        # solution link https://leetcode.com/submissions/detail/623329637/

        # res = None
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None
        # forum solution: can also use recursion
        # solution link https://leetcode.com/problems/search-in-a-binary-search-tree/discuss/148890/Python-3-lines-DFS-solution-w-a-very-simple-approach
