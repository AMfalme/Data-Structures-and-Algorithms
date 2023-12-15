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

    

solution number 2:

- use hash map to solve this.
"""
def solution(s, k):
    # start_pos = 0
    # second_pointer = 0
    # longest_substring = 0
    # substring_dict = {}
    # print(arr)
    # characters = []
    window_start = 0
    max_length = 0
    characters = {}
    for i, value in enumerate(s):
        characters[value] = characters.get(value, 0) + 1

        while len(characters) > k:
            characters[s[window_start]] -= 1

            if characters[s[window_start]] == 0:
                del characters[s[window_start]]
            

            window_start += 1
            max_length = max(max_length, i - window_start + 1)
        
    return max_length


    #     if v in substring_dict.keys() and len(substring_dict.keys()) <= k and substring_dict[]:
    #         substring_dict[v] = 1
    #     if len(substring_dict.keys()) >= k:
    #         print('we have reaached k distinct characters')
    #         break
        
    #     else:
    #         substring_dict[v] = 1
    #         # longest_substring = max(longest_substring, len(substring))
    #         start_pos += 1
    #     print(v, substring_dict)
    #     # longest_substring = max(longest_substring, len(substring))
    # print(longest_substring)
    #     # print(i)
        
        # print(substring)
    #     print()
    # distinct_chars = []
    # len_of_sub_arr = 0
    # for i, v in enumerate(arr):
    #     if v in distinct_chars:
    #         len_of_sub_arr += 1
            
    #     else:
    #         distinct_chars.append(v)
    #         if len(distinct_chars) == k:


print(solution('araaci' , k =2))
print(solution('abcdeffg' , k =3))
