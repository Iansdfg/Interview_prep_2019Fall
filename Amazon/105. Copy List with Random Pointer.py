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
        dummy = new_curr = RandomListNode(0)
        while curr:
            new_node = RandomListNode(curr.label)
            new_curr.next = new_node
            
            old_to_new[curr] = new_node
            
            new_curr = new_curr.next
            curr = curr.next
            
        old_curr = head
        new_curr = dummy.next
        while old_curr:
            if old_curr.random:
                new_curr.random = old_to_new[old_curr.random]
            
            old_curr = old_curr.next
            new_curr = new_curr.next
            
        return dummy.next
