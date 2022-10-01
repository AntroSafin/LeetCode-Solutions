class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        def travel(matrix,row,col):
            if(row<0 or col<0 or row>len(matrix)-1 or col>len(matrix[0])-1 or matrix[row][col] == '*'):
                return
            ans.append(matrix[row][col])
            matrix[row][col] = '*'
            #for controlling where to start the right again(this if condition below)
            if(col+1>=row):
                travel(matrix,row,col+1)
            travel(matrix,row+1,col)
            travel(matrix,row,col-1)
            travel(matrix,row-1,col)
        travel(matrix,0,0)
        return ans
