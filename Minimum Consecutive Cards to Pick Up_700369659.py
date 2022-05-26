import sys
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        maps = {}
        i =0
        j = 0
        minLen = sys.maxsize
        
        for i in range(len(cards)):
            if cards[i] in maps and maps[cards[i]] >= j:
                cur_len = i-maps[cards[i]]+1
                minLen =min(minLen, cur_len)
                j = maps[cards[i]] + 1
                
            maps[cards[i]] = i
            
        return (minLen if minLen != sys.maxsize else -1)
            
        
