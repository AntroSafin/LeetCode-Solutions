"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

"""

#MY SOLUTION:
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

#OPTIMAL SOLUTION:
def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    R = len(matrix)
    C = len(matrix[0])
    rows, cols = set(), set()

    # Essentially, we mark the rows and columns that are to be made zero
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # Iterate over the array once again and using the rows and cols sets, update the elements
    for i in range(R):
        for j in range(C):
            if i in rows or j in cols:
                matrix[i][j] = 0
