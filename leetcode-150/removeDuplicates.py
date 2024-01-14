class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 0
        times = 1
        current_item = nums[p]
        for i in range(1,len(nums)-1):
            if nums[i] != current_item:
                times=1
                current_item = nums[i]
            elif times < 2:
                times+=1
            else:
                nums.pop(i)
                p = i
        print(nums)
        return p
    
print(Solution().removeDuplicates([1,1,1,2,2,3]))