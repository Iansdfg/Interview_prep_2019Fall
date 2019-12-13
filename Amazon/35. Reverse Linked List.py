"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        prev = None
        curr = head
        while curr:
            nextt = curr.next 
            curr.next = prev
            prev = curr
            curr = nextt
        return prev
            
