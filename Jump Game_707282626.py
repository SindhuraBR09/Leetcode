class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        destination = len(nums)-1
        for i in range(len(nums)-1, -1,-1):
            if nums[i] >= destination-i:
                destination = i
#                 canReach = True
#             else:
#                 canReach = False
                
        return True if not destination else False
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(nums)
        # shouldReach = n-1
        
#         for i in range(n-2,-1,-1):
            
#             if nums[i] >= shouldReach - i:
#                 shouldReach = i
                
#         if shouldReach == 0:
#             return True
#         else:
#             return False
            
        
