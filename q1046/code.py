# question link
from typing import List
import math
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # # solution 1: not too bad runtime as previously thought due to constant sort. Superior memory. Time 16 mins
        # # solution link https://leetcode.com/problems/last-stone-weight/submissions/921352233/?envType=study-plan&id=level-1
        # if len(stones) < 2:
        #     return stones[-1]

        # while len(stones) >= 2:
        #     stones.sort()
        #     y = stones.pop()
        #     x = stones.pop()
        #     if y > x:
        #         stones.append(y-x)
        # return stones[-1] if len(stones) == 1 else 0

        # # solution 2: too much time put into binary insert...
        # # solution link

        # def insert_sorted_array(w):
        #     # for i in range(0, len(stones)):
        #     #     upper_bound = stones[i+1] if i < len(stones)-1 else math.inf
        #     #     if stones[i] <= w <= upper_bound:
        #     #         return stones.insert(i, w)
        #     # return stones.append(w)

        #     # using binary search for index to insert
        #     start, end = 0, len(stones)-1
        #     while start < end:
        #         mid = start + (end - start) // 2
        #         if stones[mid] < w:
        #             start = mid+1
        #         elif stones[mid] > w:
        #             end = mid
        #         else:
        #             return stones.insert(mid, w)
        #     stones.insert(end+1 if end == len(stones)-1 else end, w)

        # if len(stones) < 2:
        #     return stones[-1]

        # stones.sort()
        # while len(stones) >= 2:
        #     y = stones.pop()
        #     x = stones.pop()
        #     if y > x:
        #         insert_sorted_array(y-x)

        # return stones[-1] if len(stones) == 1 else 0

        # forum solution: using heap, technique not learned yet.
        # solution link: https://leetcode.com/problems/last-stone-weight/solutions/294956/java-c-python-priority-queue/t
        h = [-x for x in stones]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]
