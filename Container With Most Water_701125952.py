class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxArea = 0
        i = 0
        j = len(height)-1
        
        while(i<j):
            temp = min(height[i], height[j])* (j-i)
            if maxArea< temp:
                maxArea = temp
            if(height[i] < height[j]):
                i = i+1
            else:
                j = j-1
                            
        return maxArea
        
