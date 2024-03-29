# question link
# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/
# https://leetcode.com/problems/binary-tree-level-order-traversal/


from typing import List, Optional
from binary_tree.base import TreeNode
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # # # solution 1: inferior performance
        # # # solution link https://leetcode.com/submissions/detail/621995488/
        # res = []
        # if not root:
        #     return []
        # queue = deque([[root]])
        # while queue:
        #     nodes = queue.popleft()
        #     res.append([node.val for node in nodes])
        #     queue_nodes = []
        #     for node in nodes:
        #         if node.left:
        #             queue_nodes.append(node.left)
        #         if node.right:
        #             queue_nodes.append(node.right)
        #     if queue_nodes:
        #         queue.append(queue_nodes)

        # return res
        # # solution 2: revisit on 2/20/2023.  still inferior performance
        # # solution link https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/901943794/
        dq = deque()
        if not root:
            return None
        dq.append([root])
        re = []

        while dq:
            nodes = dq.popleft()
            node_val = []
            level = []

            for node in nodes:
                node_val.append(node.val)
                for child in (node.left, node.right):
                    if child:
                        level.append(child)
            if level:
                dq.append(level)
            if node_val:
                re.append(node_val)

        return re

        # forum solution: looks more pythonic with list comprehension. No improvement in performance
        # https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33464/5-6-lines-fast-python-solution-(48-ms)
