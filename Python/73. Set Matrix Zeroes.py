class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def change(matrix,row,col):
            for i in range(len(matrix)):
                matrix[i][col] = 0
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
        zeroes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j] == 0):
                    zeroes.append([i,j])
        for i,j in zeroes:
            change(matrix,i,j)
