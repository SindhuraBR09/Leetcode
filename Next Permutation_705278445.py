class Solution(object):
    def nextPermutation(self, nums):
        
        
                
#         i = len(nums)-2
#         start = 0
#         found = False
#         while(i >= 0):
#             if nums[i+1] > nums[i]:
#                 start = i
#                 found = True
#                 break                
#             else:
#                 i = i-1  
        
#         if start >=0:
#             i = len(nums)-1
#             while(i != start):
#                 if nums[i] > nums[start]:
#                     nums[start], nums[i] = nums[i], nums[start]
#                     break
#                 i = i-1
            
#         i = start+1
#         j = len(nums)-1
#         while(i<j):
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1
#             j -= 1
        
         
            
        i = len(nums)-1
        
        while(i > 0 and nums[i] <= nums[i-1]):
            i = i-1
            
        if i-1 >= 0:
            j = len(nums) -1
            while(nums[j] <= nums[i-1] and j != i-1):
                j = j-1
                
            nums[i-1], nums[j] = nums[j], nums[i-1]
            
        start = i
        end = len(nums)-1
        while(start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start = start +1
            end = end -1
            
            
            

            
        
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
