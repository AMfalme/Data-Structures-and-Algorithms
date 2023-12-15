# Given a string, find the length of the longest 
# substring in it with no more than k distinct 
# characters.
# input = [a,r,a,a,c,i] , k =2
# output = 4
"""


[a, r, a, a, c, i]


loop through arr
- have list of available letters and subsequent count
turn above list to this
{
'a': 1,
'r': 1,
'a': 2,
'c': 1,
'i': 1
}
longest_substring = 
key_letters = []
now loop through the keys.
if len(key_letters) < k:
    add 

    

solution a 2:

- use hash map to solve this.
"""
def solution(s, k):
    start_pos = 0
    characters = {}
    max_len = 0
    for i, v in enumerate(s):
        characters[v] = characters.get(v, 0) + 1
        while len(characters) > k:
            characters[s[start_pos]] -= 1
            if characters[s[start_pos]] == 0:
                del characters[s[start_pos]]
            start_pos += 1
        max_len = max(max_len,i - start_pos+1)
    return max_len


print(solution('araaci' , k =2), 4)
print(solution('abcdeffg' , k =3), 4)
print(solution('cbbebi', k=3), 5)