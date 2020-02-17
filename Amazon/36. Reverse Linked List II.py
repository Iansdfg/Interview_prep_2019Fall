"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        dummy = ListNode(-1, head)
        
        m_pre = self.find_kth(dummy, m-1)
        mth = m_pre.next 
        nth = self.find_kth(dummy, n)
        n_next = nth.next
        nth.next = None 
        
        self.reverse(mth)
        m_pre.next = nth
        mth.next = n_next
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
