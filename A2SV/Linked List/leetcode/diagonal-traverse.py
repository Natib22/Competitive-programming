from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        up = True
        
        while row < m and col < n:
            result.append(mat[row][col])
            
            if up:
                while row > 0 and col < n - 1:
                    row -= 1
                    col += 1
                    result.append(mat[row][col])
                if col == n - 1:
                    row += 1
                else:
                    col += 1
            else:
                while row < m - 1 and col > 0:
                    row += 1
                    col -= 1
                    result.append(mat[row][col])
                if row == m - 1:
                    col += 1
                else:
                    row += 1
            
            up = not up
        
        return result

            

        