# Given an array of positive numbers and a positive number `S`, 
# find the length of the smallest contiguous subarray
#  whose sum is greater than or equal to `S`. Return 0 if no such subarray exists.
#  input: [2, 1, 5, 2, 3, 2], S = 7
#  output = 2


def solution(arr, s):
    window_pos = 0
    sum = 0
    min_Len = len(arr)+1
    for i, v in enumerate(arr):
        sum += v
        while sum >= s:
            min_Len = min(min_Len, i - window_pos + 1)
            sum -= arr[window_pos]
            window_pos += 1
    if min_Len == len(arr) + 1:
        return 0 
    return min_Len 

print(solution([2, 1, 5, 2, 3, 2], 7))
print(solution([2, 1, 5, 2, 8], 7))