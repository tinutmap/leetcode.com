# https://leetcode.com/problems/permutations/
from typing import List


class Solution:
    # # solution 1: https://leetcode.com/submissions/detail/612445064/
    # # inferior
    # def permute(self, nums: List[int]) -> List[List[int]]:

    #     l = len(nums)
    #     res = [None] * l
    #     all_res = []

    #     def recurse(index):
    #         if index < l:
    #             for num_index, num in enumerate(nums):
    #                 if num is not None:
    #                     res[index] = num
    #                     nums[num_index] = None
    #                     recurse(index+1)
    #                     nums[num_index] = num
    #         else:
    #             all_res.append(res[:])

    #     recurse(0)
    #     return all_res

    # solution 2: improved upon solution 1 using dict d. Better performance
    # https://leetcode.com/submissions/detail/612939768/
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     l = len(nums)
    #     if l <= 1:
    #         return [nums]
    #     d = {key: True for key in nums}
    #     res = [None] * l
    #     all_res = []

    #     def recurse(index):
    #         if index < l:
    #             for key, values in d.items():
    #                 if values:
    #                     res[index] = key
    #                     d[key] = False
    #                     recurse(index+1)
    #                     d[key] = True
    #         else:
    #             all_res.append(res[:])

    #     recurse(0)
    #     return all_res

    # solution 3: improved upon solution 2 using set s.Similar performance to solution 2
    # https://leetcode.com/problems/permutations/submissions/
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        s = set(nums)
        res = [None] * l
        all_res = []

        def recurse(index, s):
            if index < l:
                for num in s:
                    res[index] = num
                    recurse(index+1, s-{num})
            else:
                all_res.append(res[:])

        recurse(0, s)
        return all_res

    # # forum solution: good point using list slicing that makes the code more concise
    # https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS).
    # # DFS
    # def permute(self, nums):
    #     res = []
    #     self.dfs(nums, [], res)
    #     return res

    # def dfs(self, nums, path, res):
    #     if not nums:
    #         res.append(path)
    #         # return # backtracking
    #     for i in range(len(nums)):
    #         self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
