class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        if len(nums) == 1:
            return nums[-1]
            
        max_p, min_p = [0] * len(nums), [0] * len(nums)
        max_p[0], min_p[0] = nums[0], nums[0]
        res = float('-inf')
        for i in range(1, len(nums)):
            
            max_p[i] = max(nums[i], max(max_p[i - 1] *nums[i], min_p[i - 1] *nums[i]))
            min_p[i] = min(nums[i], min(max_p[i - 1] *nums[i], min_p[i - 1] *nums[i]))
            
            res = max(res, max_p[i])
            
        return res 
