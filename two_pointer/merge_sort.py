arr, array2 = [45,2,34,55,645] , [4,234,56,657,9]

# n = len(arr)
# m = len(array2)
# final_arr = [None] * (m+n)

# start with merging two sorted arrays

def merge_two_sorted_arr(arr, array2, result):
    i, j, k = 0, 0, 0

    while i+j < len(result):
        if j == len(array2) or (i < len(arr) and arr[i] < array2[j]):
            result[k] = arr[i]
            i += 1
            k += 1
        else:
            result[k] = array2[j]
            j += 1
            k += 1

    
    return result

print(merge_two_sorted_arr([1,3,4, 8, 10], [1, 2, 6, 9, 11], [None] * 10))


