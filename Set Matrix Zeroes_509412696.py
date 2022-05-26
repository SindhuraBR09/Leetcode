class Solution(object):
    def setZeroes(self, matrix):
        
        rows = []
        cols = []
        
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        for i in range(nrow):
            for j in range(ncol):
                if (matrix[i][j] == 0):
                    if i not in rows:
                        rows.append(i)
                    if j not in cols:
                        cols.append(j)
        for i in rows:
            for j in range(ncol):
                matrix[i][j] = 0
        for i in range(nrow):
            for j in cols:
                matrix[i][j] = 0
        
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
