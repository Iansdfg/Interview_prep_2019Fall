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
        curr_max = [0] * n
        max_sums = [0] * n
        
        curr_sum = 0
        max_sum = float('-inf')
        for pos, num in enumerate(nums):
            curr_sum += num
            curr_max[pos] = curr_sum
            max_sum = max(max_sum, curr_sum)
            max_sums[pos] = max_sum
            if curr_sum < 0:
                curr_sum = 0
                
        return max_sums[-1]
        
