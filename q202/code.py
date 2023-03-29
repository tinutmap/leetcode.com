# question link https://leetcode.com/problems/happy-number/?envType=study-plan&id=level-2

import functools


class Solution:
    def isHappy(self, n: int) -> bool:
        # # solution 1: bad runtime, great memory, probably due to using set. Time 40 mins for an easy q, ouch! And needs to master reduce or accumulate function.
        # # solution link https://leetcode.com/problems/happy-number/submissions/924278276/?envType=study-plan&id=level-2
        # history = set([n])
        # n_array = list(str(n))
        # while True:
        #     new_num = 0
        #     for num in n_array:
        #         new_num += int(num)**2

        #     n_array = list(str(
        #         new_num
        #     ))
        #     if len(n_array) == 1 and n_array[0] == '1':
        #         return True
        #     if new_num in history:
        #         return False
        #     history.add(new_num)

        # solution 2: great runtime, OK memory. Solution based on solution 1 Time plust reduce function.
        # solution link https: // leetcode.com/problems/happy-number/submissions/924292594 /?envType = study-plan & id = level-2
        history = set([n])
        n_array = list(str(n))
        while True:
            new_num = functools.reduce(
                lambda x, y: x + int(y)**2, n_array, 0)

            n_array = list(str(
                new_num
            ))
            if len(n_array) == 1 and n_array[0] == '1':
                return True
            if new_num in history:
                return False
            history.add(new_num)


# forum solution: more elegant code using sum and list comprehension.
# solution link https://leetcode.com/problems/happy-number/solutions/56915/my-python-solution/
