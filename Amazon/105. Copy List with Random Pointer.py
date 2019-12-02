"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        old_to_new = dict()
        dummy = dummy_curr = Node(-1, None, None)
        curr = head 
        while curr:
            new_curr = Node(curr.val, None, None)
            dummy_curr.next = new_curr
            old_to_new[curr] = new_curr
            dummy_curr = dummy_curr.next
            curr = curr.next
            
        
        curr = head 
        while curr:
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next
        return dummy.next
    
    
    
