class Solution:
    def expandAround(self,s, left, right, maxlen, start):
        if (left > right):
            return 0
        
        while(left >= 0 and right< len(s) and s[left] == s[right]):
            left = left-1
            right = right+1
            
        if maxlen < right - left -1:
            # print("Current maxlen and start {} {}", maxlen, start)
            maxlen = right - left -1
            start = left+1
            # print("changed maxlen and start {} {}", maxlen, start)
            
        return maxlen,start
        
    def longestPalindrome(self, s: str) -> str:
        
        maxlen = 0
        start = 0
        
        for i in range(0, len(s)):
            maxlen, start = Solution.expandAround(self,s,i,i,maxlen, start)
            maxlen, start = Solution.expandAround(self,s, i, i+1, maxlen, start)
            
        # print(start, maxlen)
        return s[start:start+maxlen]
                     
            
        
