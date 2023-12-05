lass Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        k = 0
        nums3 = [None] * (m + n)
        while i < m and j < n:
            if (nums1[i] < nums2[j]):
                nums3[k] = nums1[i]
                k += 1
                i += 1
            else:
                nums3[k] = nums2[j]
                j += 1
                k += 1
        while i < m:
            nums3[k] = nums1[i]
            i += 1
            k += 1

        while j < n:
            nums3[k] = nums2[j]
            j += 1
            k+= 1
        
        nums1 = nums3
       