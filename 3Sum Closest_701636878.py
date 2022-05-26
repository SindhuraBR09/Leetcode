import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        res = []
        nums = sorted(nums)
        print(nums)
        closest = sys.maxsize
        
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while(j<k):                
                total =  nums[j]+nums[k]+nums[i]
                
                if nums[j]+nums[k]+nums[i] == target:
                    return nums[j]+nums[k]+nums[i]
                
                if (abs(target-total) < abs(closest)):
                    closest = (target-total)                
                        
                if nums[i] + nums[j]+nums[k] > target:
                    k = k-1
                    
                else:
                    j = j+1
                    
        return target - closest
