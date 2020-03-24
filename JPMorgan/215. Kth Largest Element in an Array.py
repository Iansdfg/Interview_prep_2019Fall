from heapq import heapify, heappop, heappush
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k + 1
        heapify(nums)
        while k:
            top = heappop(nums)
            k -= 1
        return top
