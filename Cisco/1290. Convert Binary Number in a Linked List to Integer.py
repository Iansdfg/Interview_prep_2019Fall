# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        cur,ans = head,0
        while cur:
            ans = ans*2 + cur.val
            cur = cur.next
        return ans



        
