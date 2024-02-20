mymap = {}
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if n in  mymap:
            return mymap[n]
        mymap[n]= self.fib(n-1)+ self.fib(n-2) 
        return self.fib(n-1)+ self.fib(n-2)        