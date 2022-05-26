class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def findCombs(self, arr, target, start, k):
            
            if k == 0 and target == 0:
                res.append(arr[:])
                return
            if k == 0:
                return
            
            for i in range(start, 10):
                findCombs(self, arr+[i], target-i, i+1, k-1)
                
                
        res =[]
        findCombs(self, [], n, 1, k)
        return res
