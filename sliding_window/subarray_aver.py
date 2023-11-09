#  Given an array, find the average of all contiguous subarrays of size "K" in it.
# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2]
# k = 5
# 
# 
# 



def subarray_aver(arr, k):
    aver = []
    sum = 0
    pos = 0
    for i, v in enumerate(arr):
        sum += v
        if i >= (k-1):
            aver.append(sum / k)
            sum -= arr[pos]
            pos += 1
    return aver


print(subarray_aver([1, 3, 2, 6, -1, 4, 1, 8,2], 5))