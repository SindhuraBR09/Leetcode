# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        nextHead = ListNode()
        cur = head
        prev = nextHead
        
        if head and head.next == None:
            return head
            
        while(cur != None and cur.next != None):
            temp = cur.next.next
            prev.next = cur.next
            cur.next.next = cur
            cur.next = temp
            prev = cur
            cur = cur.next
            
            
        return nextHead.next  
