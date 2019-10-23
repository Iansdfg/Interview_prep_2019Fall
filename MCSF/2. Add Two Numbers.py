# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = dummy = ListNode(-1)
        increment = 0 
        while l1 or l2 or increment:
            summ = increment
            if l1:
                summ += l1.val
                l1 = l1.next
            if l2:
                summ += l2.val
                l2 = l2.next
            val = summ % 10
            new_node = ListNode(val)
            curr.next = new_node
            curr = curr.next
            increment = summ // 10
        return dummy.next
        
