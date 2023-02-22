# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children

    def __repr__(self) -> str:
        return f"{self.val}"


def make_tree(l: List):
    if not l:
        return None
    root = TreeNode(l[0])
    dq = deque([root])
    i = 2
    try:
        while dq:
            node = dq.popleft()
            children_node = []
            while i < len(l) and l[i]:
                child_node = TreeNode(l[i])
                children_node.append(child_node)
                i += 1
            node.children = children_node
            dq.extend(children_node)
            i += 1
    except:
        pass
    return root


def to_list(node: TreeNode) -> List:
    if node is None:
        return []
    res = [node.val]
    queue = deque([node])
    while queue:
        node = queue.popleft()
        for branch in (node.left, node.right):
            if branch:
                res.append(branch.val)
                queue.append(branch)
    return res
