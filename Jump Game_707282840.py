class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        canReach = False
        destination = len(nums)-1
        for i in range(len(nums)-1, -1,-1):
            if nums[i] >= destination-i:
                destination = i
                canReach = True
            else:
                canReach = False
                
        return canReach
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        n = len(nums)
        shouldReach = n-1
        
#         for i in range(n-2,-1,-1):
            
#             if nums[i] >= shouldReach - i:
#                 shouldReach = i
                
#         if shouldReach == 0:
#             return True
#         else:
#             return False
            
        
