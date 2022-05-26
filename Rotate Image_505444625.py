class Solution(object):
    def rotate(self, matrix):
        nRows = len(matrix)
        nCols = nRows
        
        i=0
        j =0
        
        while(i< nRows):
            
            j = i+1
            while(j<nCols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j=j+1
            i=i+1
        
        i=0
        j=0
        while(i<nRows):
            j=0
            while(j < nRows//2):
                matrix[i][j], matrix[i][nRows-1-j] = matrix[i][nRows-1-j], matrix[i][j]
                j=j+1
            i=i+1
            
        
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
