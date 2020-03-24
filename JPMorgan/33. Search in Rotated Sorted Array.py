class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1 
        left, right = 0, len(nums) - 1
        start, end = nums[0], nums[-1]
        
        while left + 1 < right:
            mid = (left + right)//2
            
            if nums[mid] <= end:
                if nums[mid] <= target <= end:
                    left = mid
                else:
                    right = mid
            elif nums[mid] > end:
                if start <= target <= nums[mid]:
                    right = mid 
                else:
                    left = mid
                    
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
