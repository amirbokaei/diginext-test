def q2(s: str):
    count = 0
    s = list(s)
    s_len = len(s)
    for i in range(s_len):

        if i == 0:
            if s[i+1] == s[i]:
                s[i] = None
                count += 1
                
        elif i == s_len-1:
            if s[i-1] == s[i]:
                s[i] = None
                count += 1
                
        elif s[i-1] == s[i] or s[i+1] == s[i]:
            s[i] = None
            count += 1

    return count
        


print(q2(input()))