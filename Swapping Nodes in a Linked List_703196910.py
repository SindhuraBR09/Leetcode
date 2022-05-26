# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        first = dummy
        last = head
        temp = dummy
        
        for i in range(1, k+1):
            first = first.next
        
        temp = first
        while(first and first.next!= None):
            last = last.next
            first = first.next
            
        print(temp.val, last.val)
        temp.val,last.val = last.val, temp.val
        
        return  dummy.next
            
        
