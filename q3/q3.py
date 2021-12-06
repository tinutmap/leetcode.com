def lengthOfLongestSubstring(s: str) -> int:
    # # first solution
    # max_length = 1
    # for i in range(len(s)):
    #     l = [s[i]]
    #     for j in s[i+1::]:
    #         if j not in l:
    #             l.append(j)
    #         else:
    #             break
    #     if len(l) > max_length:
    #         max_length = len(l)
    # return max_length

    max_len = 0
    max_sub_st = []
    for char in s:
        try:
            char_index = max_sub_st.index(char)
            max_sub_st = max_sub_st[char_index+1::]
            max_sub_st.append(char)
        except ValueError:
            max_sub_st.append(char)
        finally:
            if len(max_sub_st) > max_len:
                max_len = len(max_sub_st)
    return max_len

    # most voted solution
    # start = maxLength = 0
    # usedChar = {}

    # for i in range(len(s)):
    #     if s[i] in usedChar and start <= usedChar[s[i]]:
    #         start = usedChar[s[i]] + 1
    #     else:
    #         maxLength = max(maxLength, i - start + 1)

    #     usedChar[s[i]] = i

    # return maxLength


lengthOfLongestSubstring("pwwkew")
