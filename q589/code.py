# question link https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/?envType=study-plan&id=level-1
from typing import List
import collections
from n_rary_tree.base import TreeNode as Node


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # solution 1: OK submission
        # solution link https://leetcode.com/problems/n-ary-tree-preorder-traversal/submissions/901934031/
        if not root:
            return None
        dq = collections.deque()
        dq.append(root)
        re = []

        while dq:
            node = dq.popleft()
            re.append(node.val)
            node.children.reverse()
            for child in node.children:
                if child:
                    dq.appendleft(child)

        return re

        # forum solution: https://leetcode.com/problems/n-ary-tree-preorder-traversal/solutions/786364/python-iterative-recursive-explanation/
        # solution link
