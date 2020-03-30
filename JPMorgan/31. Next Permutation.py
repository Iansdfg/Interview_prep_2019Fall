class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        peak  = len(nums) - 1
        while peak > 0 and nums[peak] <= nums[peak-1]:
            peak -= 1 
        # print(nums[peak])
        low = peak - 1 
        
        if peak != 0:
            betwenn = len(nums) - 1
            while betwenn > 0 and nums[betwenn] <= nums[peak-1]:
                betwenn -= 1 
            # print(nums[betwenn])

            nums[betwenn], nums[low] = nums[low], nums[betwenn]
        
        self.swap(nums, peak, len(nums) - 1)
        
    def swap(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
        
        
        
            
        
