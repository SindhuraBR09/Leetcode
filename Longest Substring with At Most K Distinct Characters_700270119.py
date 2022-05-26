class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        maps = {}
        i = 0
        j = 0
        maxLen = 0
        counter = 0
        for i in range(len(s)):
            
            maps[s[i]] = i
            
            if len(maps) > k:
                index = min(maps.values())
                del maps[s[index]]
                j = index+1
            
            maxLen = max(maxLen, i-j+1)
            
        return maxLen
