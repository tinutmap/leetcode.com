from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)

    def to_list(self):
        l = []
        while self:
            l.append(self.val)
            self = self.next
        return l


class SinglyLinkedList:
    def __init__(self, l: List = [],):
        self.head = None
        if l:
            self.head = ListNode(l[0])
            cur = self.head
            for i in range(1, len(l)):
                node = ListNode(l[i])
                cur.next = node
                cur = node
