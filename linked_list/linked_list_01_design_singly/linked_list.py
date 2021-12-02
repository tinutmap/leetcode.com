# https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
from typing import List
'''
# Solution 1: using dict to store nodes
class MyLinkedList:
    def __init__(self, l: List = None, head: int = None):
        # if l is not None:
        self.head = head
        self.data = {}
        if l is not None:
            for i in range(len(l)):
                # self.data[i] = Node()
                # self.data[i].value = l[i]
                if i != len(l)-1:
                    self.data[l[i]] = l[i+1]
                else:
                    self.data[l[i]] = None

    def get(self, index: int) -> int:
        cur = self.head
        for _ in range(index):
            if cur is not None:
                cur = self.data[cur]
        return cur

    def addAtHead(self, val: int) -> None:
        head = self.head
        self.data[val] = head
        self.head = val

    def addAtTail(self, val: int) -> None:
        # traverse thru entire linked list
        cur = self.head
        while self.data[cur] is not None:
            cur = self.data[cur]

        # add at tail
        self.data[cur] = val
        self.data[val] = None

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.get(index)
        pre = self.get(index-1)
        # # traverse and get prev, cur nodes:
        # for _ in range(index):
        #     pre = cur
        #     cur = self.data[cur]

        # add new node
        self.data[val] = cur
        self.data[pre] = val

    def deleteAtIndex(self, index: int) -> None:
        cur = self.get(index)
        pre = self.get(index-1)
        nxt = self.get(index+1)

        self.data[cur] = None
        self.data[pre] = nxt

    def __str__(self) -> str:
        cur = self.head
        st = str(cur)
        while cur != None:
            st += ('-->'+str(self.data[cur]))
            cur = self.data[cur]
        return st
'''


# Solution 2: using Node last
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return str(self.value)


class MyLinkedList:
    def __init__(self, l: List = None):
        self.head = None
        self.tail_index = 0
        if l is not None:
            node = Node(value=l.pop(0))
            self.head = node
            self.tail_index += 1
            for i in range(len(l)):
                next_node = Node(l[i])
                node.next = next_node
                node = next_node
                self.tail_index += 1

    def __str__(self) -> str:
        cur = self.head
        st = ''
        if cur is not None:
            while cur is not None:
                st += cur.__repr__()+'-->'
                cur = cur.next

        return st+'None'

    def get(self, index: int) -> int:
        cur = self.head
        for _ in range(index):
            if cur is not None:
                cur = cur.next
        return cur if cur is not None else Node(-1)

    def addAtIndex(self, index: int, val: int) -> None:
        cur = Node(value=val)
        prev = None if self.get(index-1) == -1 else self.get(index-1)
        nxt = None if prev is None else prev.next

        if index <= 0:  # add at head if index <=0
            cur.next = self.head
            self.head = cur
            self.tail_index += 1
        elif prev is not None:  # prev is None means index out of range -> not valid addition
            prev.next = cur
            cur.next = nxt
            self.tail_index += 1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(index=0, val=val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(index=self.tail_index, val=val)

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            cur = self.head
            if cur is not None:
                self.head = cur.next
                self.tail_index -= 1
        elif self.get(index-1) != -1:
            prev = self.get(index-1)
            cur = prev.next
            if cur is not None:
                prev.next = cur.next
                self.tail_index -= 1


'''
Good solution here
https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/discuss/778751/Very-Clean-Python-Solution
takeaway:
- utilize 'tail_index' or 'size' for case at limit(head, tail, out-of-range)
- make self.tail available for faster adding at tail https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/discuss/139689/Python-solution
'''

# a = MyLinkedList([1, 2, 3],)
# a.get(2)
# a.addAtHead(0)
# a.addAtTail(4)
# a.addAtIndex(3, 5)
# a.deleteAtIndex(5)


# a = MyLinkedList()
# a.addAtHead(1)
# print(a)
# a.addAtTail(3)
# print(a)
# a.addAtIndex(1, 2)
# print(a)
# a.get(1)
# a.deleteAtIndex(1)
# a.get(1)
# print(a)


# a = MyLinkedList()
# a.addAtHead(0)
# a.deleteAtIndex(0)
# print(a)

# a = MyLinkedList()
# a.addAtHead(1)
# a.addAtTail(3)
# a.addAtIndex(0, 2)
# a.get(1)
# print(a)
# a.deleteAtIndex(0)
# a.get(0)
# print(a)

# a = MyLinkedList()
# a.addAtIndex(0, 0)
# a.get(0)
# a.addAtIndex(1, 1)
# a.get(1)
# a.addAtIndex(3, 3)
# # a.addAtHead(-1)
# a.addAtTail(2)
# a.deleteAtIndex(2)
# a.deleteAtIndex(2)
# a.deleteAtIndex(1)
# print(a)

# a = MyLinkedList()
# a.addAtHead(7)
# a.addAtHead(2)
# a.addAtHead(1)
# a.addAtIndex(3, 0)
# a.deleteAtIndex(2)
# a.addAtHead(6)
# a.addAtTail(4)
# a.get(4)

# a = MyLinkedList()
# a.addAtHead(1)
# a.addAtTail(3)
# a.addAtIndex(1,2)
# a.get(1)
# a.deleteAtIndex(0)
# a.get(0)

# a = MyLinkedList()
# a.addAtHead(4)
# a.addAtTail(3)
# a.addAtIndex(1, 2)
# a.get(1)
# a.deleteAtIndex(1)
# a.get(1)
