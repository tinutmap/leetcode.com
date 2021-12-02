# https://leetcode.com/problems/reverse-words-in-a-string-iii/

def reverseWords(s: str) -> str:
    # # Solution 1:
    # l = s.split(' ')
    # for i in range(len(l)):
    #     l[i] = list(l[i])
    #     for j in range(0, len(l[i])//2):
    #         if l[i][j] != l[i][len(l[i]) - j - 1]:
    #             l[i][j], l[i][len(l[i]) - j - 1] = \
    #                 l[i][len(l[i]) - j - 1], l[i][j]
    #     l[i] = ''.join(l[i])
    # return ' '.join(l)

    # Solution 2:
    l = s.split(' ')
    for i in range(len(l)):
        l[i] = list(l[i])
        l[i].reverse()
        l[i] = ''.join(l[i])
    return ' '.join(l)


reverseWords("Let's take LeetCode contest")
reverseWords("God Ding")

'''
# brilliant solution from https://leetcode.com/problems/reverse-words-in-a-string-iii/discuss/101909/1-line-Ruby-Python!
s="God Ding"
s.split() = "['God', 'Ding']
s.split()[::-1] = ['Ding', 'God'] # ?
' '.join(s.split()[::-1]) = 'Ding God'
' '.join(s.split()[::-1])[::-1] = 'doG gniD'

'''
