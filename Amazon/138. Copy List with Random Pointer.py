"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head
        old_to_new = dict()
        curr = head 
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next 
            
        curr = head 
        while curr:
            if curr.next:
                nextt = curr.next
                old_to_new[curr].next = old_to_new[nextt]
        
            if curr.random:
                random = curr.random
                old_to_new[curr].random = old_to_new[random]
            curr = curr.next
            
        return old_to_new[head]
        
        
