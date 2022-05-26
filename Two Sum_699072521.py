class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        maps = {}
        i = 0        
        for i in range(0,len(nums)):
            maps[nums[i]] = i
            
        for i in range(0,len(nums)):
            temp = target - nums[i]
            if temp in maps and maps[temp] != i:
                return [i,maps[temp]]
        
                

