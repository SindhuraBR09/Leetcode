# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        
        dummy = ListNode()
        dummy.next = head
        nxt = dummy
        cur = dummy
        i = 1
        j=0
        
        while(cur!= None):
            
            while(i <= m and cur != None):
                cur = cur.next
                i = i+1
            nxt = cur    
            while(j <= n and nxt != None):
                nxt = nxt.next
                j = j+1            
                
            if cur != None:
                cur.next = nxt
            
            i = 1
            j = 0
            
        return dummy.next
            
                
            
        
