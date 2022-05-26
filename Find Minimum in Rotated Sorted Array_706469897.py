class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def findPivot(self, nums, start, end):
            
            if nums[start] <= nums[end]:
                return nums[start]
            while(start <= end):
                mid = (start+end) // 2
                
                if nums[mid] > nums[mid+1]:
                    return nums[mid+1]
                
                elif nums[mid] < nums[start]:
                    end = mid-1
                else:
                    start = mid+1
                    
        return findPivot(self, nums, 0, len(nums)-1)
        
