class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        left , right = 0 , x//2 +1
        while left <=right:
            mid = (left+right)//2
            square = mid**2
            if square == x:
                return mid
            if square < x:
                left = mid +1
            else:
                right = mid-1
        return right
        