class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        
        dummy_matrix = obstacleGrid
        rows  = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        if (dummy_matrix[0][0] == 1):
            return 0
        
        dummy_matrix[0][0] =1
        for i in range(1,rows):
            dummy_matrix[i][0] = int(dummy_matrix[i][0] == 0 and dummy_matrix[i-1][0] == 1)
        
        for j in range(1,cols):
            dummy_matrix[0][j] = int(dummy_matrix[0][j] == 0 and dummy_matrix[0][j-1] == 1)
        
        for i in range(1, rows):
            for j in range(1, cols):
                if (dummy_matrix[i][j] == 1):
                    dummy_matrix[i][j] = 0
                else :
                    dummy_matrix[i][j] = dummy_matrix[i-1][j] + dummy_matrix[i][j-1]
        
        return dummy_matrix[rows-1][cols-1]
                    
                
                
                
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
