# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insert(self, dummy, node):
        if not dummy.next:
            dummy.next = node
        else:
            nextt = dummy.next
            dummy.next = node
            node.next = nextt
            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        increment = 0
        while stack1 or stack2 or increment:
            summ = increment
            if stack1:
                summ += stack1.pop()
            if stack2:
                summ += stack2.pop()
            val = summ % 10
            new_node = ListNode(val) 
            self.insert(dummy, new_node)
            increment = summ//10
            
        return dummy.next
