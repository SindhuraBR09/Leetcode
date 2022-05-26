class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(arr, low, high, x):
            print(high,low)
 
            if high >= low: 
                mid = (high + low) // 2

                if arr[mid] == x:
                    return mid
                elif arr[mid] > x:
                    return binary_search(arr, low, mid - 1, x)
                else:
                    return binary_search(arr, mid + 1, high, x) 
            else:
                return -1
        
        def find_pivot(nums):
            
            if nums[0] < nums[-1]:
                return 0
            #find the pivot
            i = 0
            j = len(nums)-1
            pivot = 0            

            while(i<=j):
                mid = int((i+j)/2)
                print("mid is ", mid)
                
                if nums[mid] > nums[mid+1]:
                    return mid+1  
                else:
                    if nums[mid] < nums[i]:
                        j = mid-1
                    
                    else:
                        i=mid+1

                # elif nums[mid] < nums[mid+1] and nums[mid+1] > nums[-1]:
                #     i=mid+1
                # elif nums[pivot] < nums[i]:
                #     j = mid-1
                    
            return pivot
        if (len(nums) == 1):
            if nums[0] == target:
                return 0
            else:
                return -1
            
        pivot = find_pivot(nums)
        print("pivot is ", pivot)
        if target == nums[pivot]:
            return pivot
        if pivot == 0:
            start = 0
            end = len(nums)-1
        else:
            if target < nums[0]:
                start = pivot
                end = len(nums)-1
            else: 
                start = 0
                end = pivot-1
            
        return binary_search(nums, start, end, target)
                
            
        
        
