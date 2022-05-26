from collections import deque
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates = sorted(candidates)
        res = []
        queue = deque()
        for i in candidates:
            queue.append([i])
        while(queue):
            curr = queue.pop()
            if sum(curr) == target:
                res.append(curr)
            else:    
                for i in candidates:
                    if (sum(curr) + i) == target:
                        temp = curr + [i]
                        if sorted(temp) not in res:
                            res.append(sorted(curr+[i]))

                    else:
                        if (sum(curr)+i) < target:
                            if sorted(curr+[i]) not in queue:
                                queue.append(curr+[i])
                                
        return res
                        
                    
            
        
