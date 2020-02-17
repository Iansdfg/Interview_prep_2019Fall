"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # write your code here
        dummy = ListNode(-1, head)
        prev = dummy
        kth = self.find_kth(prev, k)
        
        while kth:
            if kth == None:
                return dummy.next
            
            k_next = kth.next 
            kth.next = None 
            
            self.reverse(head)
            prev.next = kth
            head.next = k_next
    
            prev = head
            head = k_next
            kth = self.find_kth(prev, k)
        
        return dummy.next
            
    def reverse(self, head):
        prev = None 
        while head:
            nextt = head.next
            head.next = prev
            prev = head
            head = nextt
        return prev
        
    def find_kth(self, head, k):
        for _ in range(k):
            if not head:
                return None 
            head = head.next
        return head
