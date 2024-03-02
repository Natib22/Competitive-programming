class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        def my(row):
            if row == 1:
                return [1,1]
            temp = my(row-1)
            arr = [1] * (row+1)
            for i in range(1,len(arr)-1):
                arr[i] = temp[i-1] + temp[i]
            return arr
            
        if rowIndex == 0:
            return [1]
        return my(rowIndex)


        