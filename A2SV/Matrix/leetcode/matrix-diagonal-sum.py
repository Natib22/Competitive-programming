class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row , col = 0 , 0 
        mysum  = 0 
        while row < len(mat) and col < len(mat[0]):
            mysum+= mat[row][col]
            mysum+=mat[row][len(mat[0])-1-col]
            row+=1
            col+=1
      
        if len(mat)%2 == 1:
            return mysum - mat[len(mat)//2][len(mat[0])//2]
        return mysum

        