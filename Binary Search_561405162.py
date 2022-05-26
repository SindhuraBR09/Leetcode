class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        def findele(self, nums, target, low, high) :
            
            while(low <= high):
               
                mid =  (low + high) // 2
                if (target == nums[mid]):
                    return mid
                else:
                    if (nums[mid] < target):
                        return findele(self, nums, target, mid+1, high)
                    else:
                        return findele(self, nums, target, low, mid-1)
                    
            return -1
        
        return findele(self, nums, target, 0, len(nums)-1)
        
