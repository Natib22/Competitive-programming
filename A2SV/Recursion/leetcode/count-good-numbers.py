MOD = 10**9 + 7

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = n//2 
        odd = n//2 
        if n%2==1:
            even+=1
        
        ans = (self.myPow(5,even) * self.myPow(4, odd)) % MOD
        return ans 
    

    def myPow( self , x, n): 
        if n == 1:
            return x
        if n==0:
            return 1
        half = self.myPow(x,n//2)
        if n%2 == 0:
            return (half * half) % MOD
        return (x * half * half) % MOD
            
        


        
        
        
        
        
        
        
        
        



        
        
        