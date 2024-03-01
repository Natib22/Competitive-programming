class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        
        arr = list(palindrome)
        if arr == ["a"] * len(arr):
            arr[-1] = "b"
            return "".join(arr)
        
        for i in range(len(arr)):
            if arr[i] != "a":
                temp = arr[i]
                arr[i] = "a"
                if arr != ["a"] * len(arr):
                    print(arr)
                    break
                else:
                    arr[i] = temp
                    arr[-1] = "b"
                    break
        
        return "".join(arr)
        