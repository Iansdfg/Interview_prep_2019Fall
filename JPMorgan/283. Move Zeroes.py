class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # find zero
        slow = 0
        while nums[slow]:
            slow += 1 
            if slow >= len(nums):
                return 
        
        fast = slow + 1
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1 
