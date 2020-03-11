class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        num_to_count = self.get_count(arr)
        order = self.sort_by_count(num_to_count)
        
        result = 0
        count_sum = 0
        for count, num in order:
            # print(count, num)
            count_sum += count
            result += 1 
            if count_sum >= len(arr)//2:
                return result
            
    def get_count(self, arr):
        num_to_count = {}
        for num in arr:
            if num in num_to_count:
                num_to_count[num] += 1 
            else:
                num_to_count[num] = 1 
        return num_to_count
    
    def sort_by_count(self, num_to_count):
        result = []
        for key in num_to_count:
            result.append((num_to_count[key], key))
        result.sort()
        result.reverse()
        return result
            
        
