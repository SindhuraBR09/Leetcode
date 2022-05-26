## priority queue had problem in Python3. 


import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        head = ListNode(0)
        cur = temp = head
        q = []
        count = 0
        for l in lists:
            if l:
                count = count+1
                heapq.heappush(q, (l.val,count, l))

        while(len(q) > 0):
            _,_, temp = heapq.heappop(q)
            
            cur.next = temp
            temp=temp.next
            
            if temp:
                count += 1
                heapq.heappush(q, (temp.val, count, temp))
            cur=cur.next
            
        return head.next
        
        
        
      
        
