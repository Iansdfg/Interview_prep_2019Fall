from heapq import heapify, heappop, heappush
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k + 1
        heapify(nums)
        while k:
            top = heappop(nums)
            k -= 1
        return top
    
    
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        return self.helper(nums, k - 1, start, end)
    
    def helper(self, nums, k, start, end):
        # return kth largest
        if start >= end:
            return nums[start]
        
        left, right = start, end
        pivit = nums[(left + right)//2]
        
        while left <= right:
            while left <= right and nums[left] > pivit:
                left += 1 
            while left <= right and nums[right] < pivit:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1
        
        if k <= right:
            return self.helper(nums, k, start, right)
        elif k >= left:
            return self.helper(nums, k, left, end)
        else:
            return nums[k]
            
                
                
                
                
                
                
                
        
