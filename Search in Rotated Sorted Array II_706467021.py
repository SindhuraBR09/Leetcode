class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        
        def binarySearch(self, nums, start, end):
            
            while(start <= end):                
                mid = (start + end) // 2
                print(nums[mid], target)
                if target == nums[mid]:
                    return True
                else:
                    if nums[mid] == nums[start] and nums[end] == nums[mid]:
                        start = start+1
                        end = end-1
                    elif nums[mid] >= nums[start]:
                        if nums[mid] > target and nums[start] <= target:
                            end = mid-1
                        else:
                            start = mid+1
                    else: 
                        if nums[mid] < target and nums[end] >= target:
                            start = mid +1
                        else:
                            end = mid-1
            return False
        
        return binarySearch(self, nums, 0, len(nums)-1)
                    
        
