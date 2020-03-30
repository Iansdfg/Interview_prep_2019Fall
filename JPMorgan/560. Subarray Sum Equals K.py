class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        dp = [0] * (len(nums) +1)
        for i in range(1, len(nums)+1):
            dp[i] = dp[i - 1] + nums[i - 1]
            
        for start in range(len(nums)):
            for end in range(start + 1, len(nums)+1):
                if dp[end] - dp[start] == k:
                    count += 1 
                    
        return count
            
