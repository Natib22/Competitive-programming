class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        myarray =[]
        for i in range (len(matrix[0])):
            myarray.append([0] * len(matrix))
        i , j =  0 , 0 
    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                myarray[j][i] = matrix[i][j]
        return myarray


        