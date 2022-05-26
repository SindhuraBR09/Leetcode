class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def findCombinations(self, arr, start):
            
            if len(arr) == k:
                res.append(arr[:])
                return
                
            else:
                for i in range(start, n+1):
                    findCombinations(self, arr+[i], i+1)
                    
        res = []
        findCombinations(self, [], 1)
        return res            
        
