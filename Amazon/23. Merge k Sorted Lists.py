# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0 :
            return None 
        start, end = 0, len(lists)-1
        return self.merge_range_lists(lists, start, end)
    
    def merge_range_lists(self, lists, start, end):
        
        if start == end:
            return lists[start]
        
        mid = (start + end)//2
        
        left = self.merge_range_lists(lists, start, mid)
        right = self.merge_range_lists(lists, mid + 1, end)
        return self.merge_two_list(left, right)
        
    def merge_two_list(self, l1, l2):
        dummy = tail = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
                
        
        
        
        
        
        
        
