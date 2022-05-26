# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        i = 1
        j = 1
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        prev = dummy
        
        while(i <= n+1):
            cur= cur.next
            i =i+1
        
        while(cur!= None):
            cur=cur.next
            prev=prev.next
        
        # if cur == prev:
        #     prev.next = None
        #     return head
        # if prev == head:
        #     return head.next
        # else:
        prev.next = prev.next.next
        
        return dummy.next
    
    
        
