class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        top = n
        while top > 0 and nums[top] <= nums[top - 1]:
                top -= 1
        low = top - 1
                
        if top != 0:
            between = n
            while top > 0 and nums[between] <= nums[low]:
                between -= 1
            nums[between], nums[top - 1] = nums[low], nums[between]
        
        self.reverse(nums, top, n)
        
    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        
        
            
        
