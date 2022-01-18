# question link
# https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/536/
# https://leetcode.com/problems/symmetric-tree/


from typing import Optional
from binary_tree.base import TreeNode
from collections import deque


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # # solution 1: using BFS. So-so performance. Spagetti code
        # # solution link: https://leetcode.com/submissions/detail/622631797/
        # if root.left is None and root.right is None:
        #     return True
        # if root.left and root.right:
        #     queue = deque([[root.left, root.right]])
        # else:
        #     return False
        # while queue:
        #     nodes = queue.popleft()
        #     n_nodes = len(nodes)
        #     if n_nodes % 2 != 0:
        #         return False
        #     l_queue = []
        #     r_queue = deque([])
        #     for i in range(len(nodes)//2):
        #         if nodes[i].val != nodes[n_nodes-i-1].val:
        #             return False
        #         if nodes[i].val is not None:
        #             if nodes[i].left:
        #                 l_queue.append(nodes[i].left)
        #             else:
        #                 l_queue.append(TreeNode(None))
        #             if nodes[i].right:
        #                 l_queue.append(nodes[i].right)
        #             else:
        #                 l_queue.append(TreeNode(None))
        #         if nodes[n_nodes-i-1].val is not None:
        #             if nodes[n_nodes-i-1].right:
        #                 r_queue.appendleft(nodes[n_nodes-i-1].right)
        #             else:
        #                 r_queue.appendleft(TreeNode(None))
        #             if nodes[n_nodes-i-1].left:
        #                 r_queue.appendleft(nodes[n_nodes-i-1].left)
        #             else:
        #                 r_queue.appendleft(TreeNode(None))
        #     if l_queue+list(r_queue):
        #         queue.append(l_queue+list(r_queue))
        # return True

        # # solution 2: recursion. Not very good performance nor code.
        # # https://leetcode.com/submissions/detail/622738585/
        # def is_leaf(node):
        #     return node.left is None and node.right is None
        # res = True

        # def compare(l_node, r_node):
        #     nonlocal res
        #     if (l_node.val == r_node.val):
        #         if is_leaf(l_node) and is_leaf(r_node):
        #             return
        #         else:
        #             compare(l_node.left if l_node.left is not None else TreeNode(
        #                 None), r_node.right if r_node.right is not None else TreeNode(None))
        #             compare(l_node.right if l_node.right is not None else TreeNode(
        #                 None), r_node.left if r_node.left is not None else TreeNode(None))
        #     else:
        #         res = False
        # if root.left is None and root.right is None:
        #     return True
        # if root.left is None or root.right is None:
        #     return False
        # compare(root.left, root.right)
        # return res

        # solution 3: recursion. better than solution 2
        # https://leetcode.com/submissions/detail/622758105/
        def compare(l_node, r_node):
            return type(l_node) == type(r_node) and ((l_node == r_node) or (l_node.val == r_node.val and
                                                                            l_node.left == r_node.left and
                                                                            l_node.right == r_node.right))

        def is_leaf(node):
            return node == None or node.left == node.right == None

        def dfs(l_node, r_node):
            if is_leaf(l_node) or is_leaf(r_node):
                return compare(l_node, r_node)
            else:
                return l_node.val == r_node.val and dfs(l_node.left, r_node.right) and dfs(l_node.right, r_node.left)
        return dfs(root.left, root.right)
        # forum solution: better handling None leaf
        # link https://leetcode.com/problems/symmetric-tree/discuss/33068/6line-AC-python
