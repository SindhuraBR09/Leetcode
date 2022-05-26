class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def permutations(self, start):
            
            if start == n:
                if nums[:] not in res:
                    res.append(nums[:])
                
            for i in range(start, n):

                nums[i], nums[start] = nums[start], nums[i]
                permutations(self, start+1)
                nums[i], nums[start] = nums[start], nums[i]

        res = []
        n= len(nums)
        permutations(self, 0)
        return res
        
