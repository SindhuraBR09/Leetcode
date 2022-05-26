from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        arr = [[],[],['a','b','c'], ['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],
              ['p','q','r','s'],['t','u','v'], ['w','x','y','z']]
        
        res = []
        if digits == "":
            return res
        maxLen = len(digits)
        queue = deque()
        queue.append("")
        while(queue):
            curr = queue.pop()
            
            length = len(curr)
            if (length == len(digits)):
                res.append(curr)
            else:
                
                arrNext = arr[int(digits[length])]
                for i in arrNext:
                    queue.append(curr+i)
            
        return res

        
            
            
        
        
        
        
