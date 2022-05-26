class Solution(object):
    import sys
    # def findSum(self, row, col, m, n, grid):
    #     if (m>row or n > col):
    #         return sys.maxsize
    #     if(m==row and n == col):
    #         return grid[m][n]
    #     else:
    #         return grid[m][n] + min(Solution.findSum(self,row,col,m+1,n,grid), Solution.findSum(self,row,col,m,n
        +1,grid))
        
        
        
        
    def minPathSum(self, grid):
        
        row = len(grid)
        col = len(grid[0])
        
        # dist = Solution.findSum(self,row ,col,0,0, grid)
        # return dist
        
        for i in range(1,row):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for j in range(1, col):
             grid[0][j] =  grid[0][j-1] +  grid[0][j]
                
        for i in range(1,row):
            for j in range(1,col):
                grid[i][j] = grid[i][j] + min(grid[i][j-1], grid[i-1][j])
                
        return grid[row-1][col-1]
    
        
        
        
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
