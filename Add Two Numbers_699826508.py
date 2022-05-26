# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:        
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        temp = head
        val1 = 0
        val2 = 0
        carry = 0
        while(l1 or l2):
            if (not l1):
                val1 = 0
            else:
                val1 = l1.val
                
            if (not l2):
                val2 = 0
            else:
                val2 = l2.val
            carry, value = divmod(val1+val2+carry, 10)
            
            newNode = ListNode(value)
            temp.next = newNode
            temp = temp.next
            
            if (l1):
                l1 = l1.next
            if (l2):
                l2 = l2.next           
            
            
        if carry:
            
            temp.next = ListNode(carry)
            
        return head.next
            
            
        
            
        
