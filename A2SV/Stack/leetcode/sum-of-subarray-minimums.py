class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        length = len(arr)
        prev = [-1] * length
        nextSmaller = [-1] * length
        MOD = 10**9 + 7
        stack = []
        

        for i in range(length):
            while stack and arr[i] < arr[stack[-1]]:
                index = stack.pop()
                nextSmaller[index] = i
            prev[i] = stack[-1] if stack else -1
            stack.append(i)
        
 
        stack = []

   
        for i in range(length - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            nextSmaller[i] = stack[-1] if stack else -1
            stack.append(i)

        total = 0
        
      
        for i in range(length):
            left = i - prev[i] if prev[i] != -1 else i + 1
            right = nextSmaller[i] - i if nextSmaller[i] != -1 else length - i
            total += arr[i] * left * right

        return total % MOD



        