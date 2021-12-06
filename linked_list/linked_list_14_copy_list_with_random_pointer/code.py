# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1229/


# Definition for a Node.
from typing import List


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        return str(tuple(self.val, self.next, self.random))


# class InputList:
def input_list(l: List = []) -> None:
    # head = cur_node = Node(0)
    if l:
        first_l = l[0]
        head = cur_node = Node(x=first_l[0], random=first_l[1])
        for i in range(1, len(l)):
            cur_node = Node(x=l[i][0], random=l[i][1])
            cur_node = cur_node.next
    return head


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        pass
