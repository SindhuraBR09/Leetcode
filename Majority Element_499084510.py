from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        
        count = Counter(nums)
        for k in count:
            if (count[k] > len(nums)//2):
                return k
            
#         count = 0
#         candidate = None

#         for num in nums:
#             if count == 0:
#                 candidate = num
#             if (num == candidate):
#                 count = count +1
#             else :
#                 count = count -1
#             # count += (1 if num == candidate else -1)

#         return candidate


        
        """
        :type nums: List[int]
        :rtype: int
        """
        
