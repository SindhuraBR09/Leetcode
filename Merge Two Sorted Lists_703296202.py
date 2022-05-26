# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newHead = ListNode()
        cur = newHead
        while(list1 and list2):
            newNode = ListNode()            
            if list1.val < list2.val:
                newNode.val = list1.val
                list1=list1.next
            else:
                newNode.val = list2.val
                list2=list2.next
                
            cur.next = newNode
            cur = cur.next
            
        if list1:
            cur.next = list1
            
        if list2:
            cur.next = list2
            
        return newHead.next

                
        
