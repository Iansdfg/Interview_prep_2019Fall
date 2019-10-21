class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for pos, num in enumerate(nums):
            if num not in dic:
                dic[target - num] = pos
            else:
                return [dic[num], pos] 
        
        
