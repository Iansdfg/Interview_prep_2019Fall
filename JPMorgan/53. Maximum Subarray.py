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
        
