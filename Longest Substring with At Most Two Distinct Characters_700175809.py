class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        maps = {}
        i = 0
        j = 0
        k = 0
        maxLen = 0
        counter = 0
        for i in range(len(s)):
            
            maps[s[i]] = i
            
            if len(maps) > 2:
                index = min(maps.values())
                del maps[s[index]]
                j = index+1
                
            maxLen = max(maxLen, i-j+1)
            
        return maxLen
