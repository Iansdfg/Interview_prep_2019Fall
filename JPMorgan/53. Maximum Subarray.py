class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        return self.helper(nums, start, end)
        
        
    def helper(self, nums, start, end):
        if start == end:
            return nums[start]
        
        left, right = start, end
        pivot = (left + right)//2
        
        left_sum = self.helper(nums, left, pivot)
        right_sum = self.helper(nums, pivot + 1, right)
        cross_sum = self.cross_sum(nums, left, right, pivot)
        
        return max(left_sum, right_sum, cross_sum)
    
    def cross_sum(self, nums, left, right, pivot):
        if left == right:
            return nums[left]
        
        left_max = float('-inf')
        curr_sum = 0
        for i in range(pivot, left-1, -1):
            curr_sum += nums[i]
            left_max = max(left_max, curr_sum)
            
        right_max = float('-inf')
        curr_sum = 0
        for i in range(pivot + 1, right + 1):
            curr_sum += nums[i]
            right_max = max(right_max, curr_sum)
        
        return right_max + left_max
            
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        local_max = [0] * n
        global_max = [0] * n
        all_max = nums[0]
        for pos, num in enumerate(nums):
            curr_max = nums[pos] if pos == 0 else max(num, local_max[pos - 1] + num)
            local_max[pos] = curr_max
            
            all_max = max(curr_max, all_max)
            global_max[pos] = all_max
        return global_max[-1]
        
