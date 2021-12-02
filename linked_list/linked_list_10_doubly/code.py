# from typing_extensions import IntVar


class DoublyListNode:
    def __init__(self, val=None, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return str(self.val)

# Solution 1: Accepted https://leetcode.com/submissions/detail/596014358/?from=explore&item_id=1294


class MyLinkedList:

    def __init__(self, *args, **kwargs):
        self.head = DoublyListNode()
        self.len = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.len:
            return -1
        i = 0
        node = self.head
        while i < index:
            i += 1
            node = node.next
        return node

    def addAtIndex(self, index: int, val: int) -> None:
        node = DoublyListNode(val)
        if index == 0:  # edge case: add at head
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.len += 1
        else:
            cur_node = self.get(index-1)
            if cur_node != -1:
                next_node = cur_node.next

                cur_node.next = node
                node.prev = cur_node

                node.next = next_node
                # edge case: next node == None -> add at tail -> no need to add next_node.prev
                if next_node:
                    next_node.prev = node
                self.len += 1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.len, val)

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:  # edge case delete at head.
            self.head = self.head.next
            self.head.prev = None
            self.len -= 1
        else:
            cur_node = self.get(index)
            if cur_node != -1:
                prev_node = cur_node.prev
                next_node = cur_node.next

                prev_node.next = next_node
                # edge case: next node == None -> delete at tail -> no need to assign next_node.prev
                if next_node:
                    next_node.prev = prev_node
                self.len -= 1


'''
Solution: https://leetcode.com/explore/learn/card/linked-list/210/doubly-linked-list/1294/discuss/148773/Python-AC-short-and-simple-linked-list-solution
Key takeaways:
- Use tail node for tail operations (add,delelete)
- with tail node available, start from head if index in first half, and start from tail if index in last half.
'''
