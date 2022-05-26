from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        
        queue = deque()
        
        for i in s:            
            if i == '(' or i == '{' or i == '[':
                queue.append(i)
                
            else:
                if not queue:
                    return False
                else:
                    last = queue.pop()
                    if (last == '(' and i != ')') or (last == '{' and i != '}') or (last == '[' and i != ']'):
                        return False
                    
        if queue:
            return False
        else:
            return True
        
