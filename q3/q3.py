def lengthOfLongestSubstring(s: str) -> int:
    """
    # solution 1: failed
    max_length = 1
    for i in range(len(s)):
        l = [s[i]]
        for j in s[i+1::]:
            if j not in l:
                l.append(j)
            else:
                break
        if len(l) > max_length:
            max_length = len(l)
    return max_length

    """
    """
    # solution 2: passed, not so good time
    # https://leetcode.com/submissions/detail/597969245/
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
    """

    """
    # most voted solution
    start = maxLength = 0
    usedChar = {}

    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[s[i]] = i

    return maxLength
    """

    """
    # solution 3: accepted, still not so great
    # https://leetcode.com/submissions/detail/598391331/
    max_l = 0
    max_st = ''
    for f in s:
        if f not in max_st:
            max_st = max_st+f
        else:
            j = max_st.find(f)
            max_st = max_st[j+1::]+f
        max_l = max(max_l, len(max_st))
    return max_l
    """

    # solution 4: using dict instead of max_st
    # still similar performance to solution 3, not really improving
    # https://leetcode.com/submissions/detail/598403168/
    d = {}
    j = 0
    max_length = 0
    length = 0
    for l in s:
        if l not in d or d[l] == 0:
            d[l] = 1
            length += 1
        else:
            while s[j] != l:
                d[s[j]] = 0
                j += 1
                length -= 1
            # d[l] = 1
            j += 1
        max_length = max(max_length, length)
    return max_length


# lengthOfLongestSubstring("pwwkew")
