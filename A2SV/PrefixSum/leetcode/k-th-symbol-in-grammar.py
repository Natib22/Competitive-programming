class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def my(n,k):
            if n == 1:
                return 0
    
            mid = (2 ** (n - 1)) // 2
            if k <= mid:
                return my(n - 1, k)
            else:
                return 1 if my(n - 1, k - mid) == 0 else 0
        ans = my(n,k)
        return ans

        