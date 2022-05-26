from collections import deque
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def findCombinations(self, nums, target, arr, res):

            if target == 0:
                if sorted(arr) not in res:
                    res.append(sorted(arr[:]))
                return res

            if target < 0:
                return res

            else:
                for i in range(0, len(nums)):
                    arr.append(nums[i])
                    res = findCombinations(self, nums, target-nums[i], arr, res)
                    arr.pop(-1)                    
            return res
                    
            
        res = []
        res = findCombinations(self, candidates, target, [], res)
        return res
        
        
#         candidates = sorted(candidates)
#         res = []
#         queue = deque()
#         for i in candidates:
#             queue.append([i])
#         while(queue):
#             curr = queue.pop()
#             if sum(curr) == target:
#                 res.append(curr)
#             else:    
#                 for i in candidates:
#                     if (sum(curr) + i) == target:
#                         temp = curr + [i]
#                         if sorted(temp) not in res:
#                             res.append(sorted(curr+[i]))

#                     else:
#                         if (sum(curr)+i) < target:
#                             if sorted(curr+[i]) not in queue:
#                                 queue.append(curr+[i])
                                
#         return res
    
    

                
                
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                        
                    
            
        
