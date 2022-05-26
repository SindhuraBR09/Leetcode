class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:       
        
        i = 0
        j = len(nums)-1
        mid=0
        startIndex=endIndex=-1
        #find left index
        while(i<=j):
            mid= (i+j) // 2
            print(i,j,mid)
            if nums[mid] == target:
                startIndex=mid
                j = mid-1                
            elif nums[mid] < target:
                i = mid+1
            else:
                j = mid-1
         
        i=0
        j=len(nums)-1
        while(i<=j):
            
            mid= (i+j) // 2
            print("here ",i,j,mid)
            
            if nums[mid] == target:
                endIndex=mid
                i = mid+1               
            elif nums[mid] < target:
                i = mid+1
            else:
                j = mid-1
                
        
        return [startIndex, endIndex]
                
        
                
