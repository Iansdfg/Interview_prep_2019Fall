class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # from right to left find the first i that num[i] > num[i-1]
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1 
            
        # from right to left find the first j that num[j] > num[i-1]
        if i != 0:
            j = len(nums) - 1 
            while j > 0 and nums[j] <= nums[i-1]:
                j -= 1
            nums[j],  nums[i-1] =  nums[i-1], nums[j] 
        self.swapList(nums, i, len(nums) - 1)
        
    def swapList(self, nums, left, right):
        while left < right:
            nums[left],  nums[right] =  nums[right], nums[left]
            left += 1 
            right -= 1
        
        
        
        
