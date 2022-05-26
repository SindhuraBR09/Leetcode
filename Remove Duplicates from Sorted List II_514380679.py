# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        
        dummy = ListNode()
        dummy.next = head
        
        cur = ListNode()
        prev = ListNode()
        cur = head
        prev.next = head
        
        while (cur!= None):
            
            while ( cur.next != None and cur.val == cur.next.val):
                print(cur.val)
                cur = cur.next
            
            if (cur != prev.next):
                print("cur != prev.next")
                if (prev.next == dummy.next):
                    print("prev == dummy")
                    dummy.next = cur.next
                    
                prev.next = cur.next
                cur = cur.next
                
            elif (cur == prev.next):
                print("cur == prev.next")
                prev = cur
                cur = cur.next
                
        return dummy.next
            
            
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
