# question link https://leetcode.com/problems/implement-queue-using-stacks/
from collections import deque

# # solution 1: inherit deque class.
# # This is irrelevant. Question statement requires using 2 stacks
# # solution link https://leetcode.com/submissions/detail/619229410/
# class MyQueue(deque):

#     def __init__(self):
#         self = deque([])
#         # self =

#     def push(self, x: int) -> None:
#         self.append(x)

#     def pop(self) -> int:
#         return self.popleft()

#     def peek(self) -> int:
#         return self[0]

#     def empty(self) -> bool:
#         return len(self) == 0

# solution 2: using standard list. Better AC, worse SC than solution 1
# This is irrelevant. Question statement requires using 2 stacks
# https: // leetcode.com/submissions/detail/619245710/


class MyQueue(list):

    def __init__(self):
        self = []

    def push(self, x: int) -> None:
        self.append(x)

    def pop(self) -> int:
        return super().pop(0)

    def peek(self) -> int:
        return self[0]

    def empty(self) -> bool:
        return len(self) == 0


# forum solution:
# https://leetcode.com/problems/implement-queue-using-stacks/discuss/64198/Share-my-python-solution-(32ms)
# motivation behind 2-stack implementation:
# https://leetcode.com/problems/implement-queue-using-stacks/discuss/64284/Do-you-know-when-we-should-use-two-stacks-to-implement-a-queue
