class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        i = len(nums) -1     
        d = [0] * n
        longest = 0
        
        #i to check from start j too check from last. 
        
        for i in range(n-1, -1, -1):
            temp = 0
            for j in range(i+1,n,1):
                if nums[i] < nums[j] and d[j] > temp:
                    temp = d[j]
            d[i] = 1+temp
            if d[i] > longest:
                longest = d[i]
                
        return longest
        
        
