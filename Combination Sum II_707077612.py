class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        def findCombinations(self, nums, arr, target, start):
            if target == 0:
                if arr not in res:
                    res.append(arr[:])
                return
            if target < 0:
                return
            
            for i in range(start, len(nums)):
                if i>start and nums[i] == nums[i-1]:
                    continue                    
                if nums[i] > target:
                    break
                arr.append(nums[i])
                findCombinations(self, nums, arr, target-nums[i], i+1)
                arr.pop(-1)                
                
            return
        
        res = []
        findCombinations(self, candidates, [], target, 0)
        return res
                
        
        
