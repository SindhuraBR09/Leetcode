class Solution:
    def expandAround(self,s, left, right):
        count = 0
        
        if (left > right):
            return 0
        
        while(left >= 0 and right< len(s) and s[left] == s[right]):
            count = count + 1
            left = left-1
            right = right+1
            
            
        return count
    
    
    def countSubstrings(self, s: str) -> int:
        
        maxlen = 0
        start = 0
        total = 0
        for i in range(0, len(s)):
             total = total + Solution.expandAround(self,s,i,i) + Solution.expandAround(self,s, i, i+1)
            
        # print(start, maxlen)
        return total
        
    
        
