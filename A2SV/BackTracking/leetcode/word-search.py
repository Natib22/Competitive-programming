class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        myset = set()
        row , col = len(board) , len(board[0])
        def my(r , c , i):
            if i == len(word):
                return True
            if r < 0 or c <0 or r == row or c == col:
                return False
            if (r,c) in myset or word[i] != board[r][c]:
                return False
            myset.add((r,c))
            ans = my(r,c+1,i+1) or my(r+1,c,i+1) or my(r-1,c,i+1) or my(r,c-1,i+1)
            myset.remove((r,c))
            return ans
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if my(i,j,0):
                        return True
        return False
        