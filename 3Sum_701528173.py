

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums = sorted(nums)
        print(nums)
        for i in range(len(nums)):
            target = -nums[i]
            j = i+1
            k = len(nums)-1
            while(j<k):
                if nums[j]+nums[k] == target:
                    s = [nums[i], nums[j], nums[k]]
                    if s not in res:
                        res.append(s)
                    j = j+1
                    k = k-1
#                     while(j<k and nums[j] == nums[j-1]):
#                         j = j+1
#did not improve so commented
                        
                elif nums[j]+nums[k] > target:
                    k = k-1
                else:
                    j = j+1
                    
        return res
            
        
        

