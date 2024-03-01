class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        zeroes = 0
        arr = [0] * len(s)
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                zeroes+=1
            else:
                arr[i] = zeroes
      
        return sum(arr)
        