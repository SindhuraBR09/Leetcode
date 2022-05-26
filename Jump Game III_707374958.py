class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        def canreach(self, i):
            if i >= len(arr):
                return False
            if i<0:
                return False
            
            if visited[i] == 1:
                return True
            if visited[i] == 0:
                return False            
            if arr[i] == 0:
                return True
            
            
            else:
                if arr[i] >0:
                    arr[i] = -arr[i]
                    if(canreach(self,i+arr[i]) or canreach(self,i-arr[i])):
                        visited[i] = 1
                        return True
                    else:
                        visited[i] = 0
                        return False
            return False    
                
        
        visited = [-1 for i in range(len(arr))]
        if arr[start] == 0:
            return True
        return canreach(self, start) or canreach(self,start)
        
