class Solution:
    """
    @param nums: a integer array
    @return: return an integer denoting the number of non-unique(duplicate) values
    """
    def CountDuplicates(self, nums):
        # write your code here
        num_to_cnt = {}
        res = []
        for num in nums:
            if num in num_to_cnt:
                num_to_cnt[num] += 1 
                if num not in res:
                    res.append(num) 
            else:
                num_to_cnt[num] = 1 
        return res 
        
