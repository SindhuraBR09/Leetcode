class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        
        if len(nums)==2:
            return max(nums)
        
        d = [0]*len(nums)
        d[0] = nums[0]
        d[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)-1):
            d[i] = max(nums[i]+d[i-2], d[i-1])
            
        r1 = d[len(nums)-2]
        
        d[0] = 0
        d[1] = nums[1]
        
        for i in range(2, len(nums)):
            d[i] = max(nums[i]+d[i-2], d[i-1])
            
        r2 = d[-1]
        
        return max(r1,r2)
        
        
        
