class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidSubgrid(startRow, startCol):
            subgridSet = set()
            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if board[i][j] in subgridSet and board[i][j] != ".":
                        return False
                    else:
                        subgridSet.add(board[i][j])
            return True

        for i in range(len(board)):
            rowSet = set()
            colSet = set()
            for j in range(len(board[0])):
                if board[i][j] in rowSet and board[i][j] != ".":
                    return False
                else:
                    rowSet.add(board[i][j])


                if board[j][i] in colSet and board[j][i] != ".":
                    return False
                else:
                    colSet.add(board[j][i])

           
                if i % 3 == 0 and j % 3 == 0:
                    if not isValidSubgrid(i, j):
                        return False
        return True

        