class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #Have two pointers and a map
        #i : iterates through the string
        #j : points to the starting of window of current iteration. If current letter pointes by i is alrdy in 
            hashmap, check if its index is higher than j. If yes, that means it belongs to current string. Update 
            the j to maps[s[i]] + 1. If not, then it was visited in previous string. So update its new index.
        #max : maintaing the maximium length of string by taking i-j+1
        
        
        i = 0
        j = 0
        maps = {}
        maxLen = 0
        
        for i in range(len(s)):
            if s[i] in maps:
                print(i, s[i])
                if maps[s[i]]+1 > j:
                    j = maps[s[i]] + 1 #if the char is repeated within windows move j to next index of previous 
                        index of that character
            maps[s[i]] = i
            print(i,j)
            maxLen = max(maxLen, i-j+1)
            
        return maxLen
