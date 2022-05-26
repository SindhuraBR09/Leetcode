class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        total = 0
        nums = sorted(nums)
        print(nums)
        for i in range(len(nums)-2):
            target1 = target-nums[i]
            j = i+1
            k = len(nums)-1
            while(j<k):
                        
                if nums[j]+nums[k] < target1:
                    print("Current total = {}",total)
                    print("adding {}",k-j)
                    total = total + k - j 
                    j = j+1                    
                else:
                    k = k-1
                    
        return total
