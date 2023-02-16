# question link
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # solution 1: inspired by JS forum solution. Good memory but poor runtime
        # solution link https://leetcode.com/problems/isomorphic-strings/submissions/899357432/

        for i, char in enumerate(s):
            if s.find(char, i+1) != t.find(t[i], i+1):
                return False

        return True

        # # forum solution: best runtime but poor memory
        # # solution link
        # # credit https://leetcode.com/problems/isomorphic-strings/solutions/57941/python-different-solutions-dictionary-etc/
        # # https://leetcode.com/problems/isomorphic-strings/submissions/899360626/
        # return list(map(s.find, s)) == list(map(t.find, t))
