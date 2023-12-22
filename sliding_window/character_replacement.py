def characterReplacement(S, K):
    # Code here
    l, r = 0, 0
    count = {}
    res = 0
    while r < len(S):
        count[S[r]] = 1 + count.get(S[r], 0)
        print(count)
        while (r-l+1)-max(count.values())> K:
            count[S[l]] -= 1
            l += 1
                
        res = max(res, r-l+1)
        r += 1
            
    return res


print(characterReplacement('ABAB', 2))