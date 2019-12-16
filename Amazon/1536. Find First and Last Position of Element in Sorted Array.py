class Solution:
    """
    @param nums: the array of integers
    @param target: 
    @return: the starting and ending position
    """
    def searchRange(self, nums, target):
        # Write your code here.
        first = self.find_first(nums, target)
        last = self.find_last(nums, target)
        return [first, last]
    def find_first(self, nums, target):
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end 
        else:
            return -1
    
    def find_last(self, nums, target):
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                start = mid
        if nums[end] == target:
            return end 
        elif nums[start] == target:
            return start
        else:
            return -1
