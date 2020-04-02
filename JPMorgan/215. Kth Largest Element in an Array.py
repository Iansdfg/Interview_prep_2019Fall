class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0 
        end = len(nums) - 1
        return self.helprt(nums, k - 1, start, end)
        
    def helprt(self, nums, k, start, end):
        if start >= end:
            return nums[start]
        
        left, right = start, end
        pivot = nums[(left + right)//2]
        
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
               
        if k <= right:
            return self.helprt(nums, k, start, right)
        elif k >= left:
            return self.helprt(nums, k, left, end)
        else:
            return nums[k]
                
