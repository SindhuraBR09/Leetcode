class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        destination = len(nums)-1
        for i in range(len(nums)-1, -1,-1):
            if nums[i] >= destination-i:
                destination = i
        return True if not destination else False
            

