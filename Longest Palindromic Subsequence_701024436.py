class Solution:
    def palindromSubstring(self, s1, s2, t):
        
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    t[i][j] = 1+t[i-1][j-1]
                    
                else:
                    t[i][j] = max(t[i][j-1], t[i-1][j])
                    
        return t[len(s1)][len(s1)]
        
        
        
            
    def longestPalindromeSubseq(self, s: str) -> int:
        
        t = [[0 for i in range(len(s)+1)] for j in range(len(s)+1)]
        
        return Solution.palindromSubstring(self, s, s[::-1], t)
        
        

        
