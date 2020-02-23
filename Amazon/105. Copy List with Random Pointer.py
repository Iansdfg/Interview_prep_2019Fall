"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        old_to_new = dict()
        
        curr = head 
        while curr:
            new_node = RandomListNode(curr.label)
            old_to_new[curr] = new_node
            curr = curr.next
            
        curr = head 
        while curr:
            next_old = curr.next
            random_old = curr.random
            
            new_node = old_to_new[curr]
            new_node.next = old_to_new[next_old] if next_old else None
            new_node.random = old_to_new[random_old] if random_old else None
            
            curr = curr.next
            
        return old_to_new[head]
