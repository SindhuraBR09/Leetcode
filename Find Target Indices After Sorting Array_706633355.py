class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        small = 0
        count = 0
        res = []
        
        for i in nums:
            if i < target:
                small += 1
            elif target == i:
                count += 1
                
        for i in range(small, count+small):
            res.append(i)
            
        return res
            
        
