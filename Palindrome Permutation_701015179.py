class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        a = [0] * 26
        for i in range(0,len(s)):
            index = ord(s[i])-97
            a[index] = 1 - a[index]
        
        print(a)
        return True if sum(a) == 1 or sum(a) == 0 else False
        
