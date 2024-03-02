

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        arr = [[0] * n for _ in range(m)]  
        
      
        for i, j in walls:
            arr[i][j] = "W"
        for i, j in guards:
            arr[i][j] = "G"
     
        for i in range(m):
            flag = False
            for j in range(n):
                if arr[i][j] == "W":
                    flag = False
                elif arr[i][j] == "G":
                    flag = True
                elif flag:
                    arr[i][j] = 1
            flag = False
            for j in range(n-1, -1, -1):
                if arr[i][j] == "W":
                    flag = False
                elif arr[i][j] == "G":
                    flag = True
                elif flag:
                    arr[i][j] = 1

        
        for j in range(n):
            flag = False
            for i in range(m):
                if arr[i][j] == "W":
                    flag = False
                elif arr[i][j] == "G":
                    flag = True
                elif flag:
                    arr[i][j] = 1

       
        for j in range(n):
            flag = False
            for i in range(m-1, -1, -1):
                if arr[i][j] == "W":
                    flag = False
                elif arr[i][j] == "G":
                    flag = True
                elif flag:
                    arr[i][j] = 1

       
        return sum(row.count(0) for row in arr)




        




        