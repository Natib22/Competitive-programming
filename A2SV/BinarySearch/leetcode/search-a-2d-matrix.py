class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left , right = -1 , len(matrix)
        n= len(matrix[0])-1
        while right - left > 1:
            mid = (right + left) //2
            if matrix[mid][n] >= target:
               right = mid
            else:
                left = mid
        return False if right == len(matrix) else self.search(matrix[right] , target)
    
    
    def search(self , nums,target):
        left , right = -1 , len(nums)
        while right - left > 1:
            mid = (right + left) //2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        return False


        