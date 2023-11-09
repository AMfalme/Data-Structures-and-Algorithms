# Given an array of positive numbers and a positive number 'k', 
# find the maximum sum  of any contiguous subarray of size k.



def max_contiguous_sum(arr, k):
    max_sum = 0
    pos = 0
    sum = 0
    for i, v in enumerate(arr):
        sum += v
        if i >= (k-1):
            max_sum = max(sum, max_sum)
            sum -= arr[pos]
            pos += 1
    return max_sum



print(max_contiguous_sum([2,1,5,1,3,2], 3))
print(max_contiguous_sum([2, 3, 4, 1, 5], 2))