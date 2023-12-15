# Given a string, find the length of the longest substring which has no repeating characters.

# input = 'aabccbb
# output = 3

# input = "abccde"
# output = 3

# input = "abbbb"
# output = 2

def solution(arr):
    stop_pos = 0
    start_pos = 0
    longest_substring = 0
    for i, v in enumerate(arr):
        stop_pos += 1
        while v in arr[start_pos:i]:
            start_pos += 1
        longest_substring = max(longest_substring, len(arr[start_pos:stop_pos]))
        
    return longest_substring

print(solution("aabccbb"), 3)
print(solution("abccuyfhgcvhgde"), 6)
print(solution("abbbb"), 2)