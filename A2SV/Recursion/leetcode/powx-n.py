mymap = {}
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n==0:
            return 1.0
        if n < 0:
            return 1/ self.myPow(x, abs(n))
        half = self.myPow(x,n//2)

        if n%2 == 0:
            return half * half
        else:
            return x * half * half
        