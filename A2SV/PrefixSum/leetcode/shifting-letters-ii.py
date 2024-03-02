class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        res = list(s)
        arr = [0] * (len(s)+1)
        for start,end , flag in shifts:
            if flag == 1:
                arr[start] += 1
                arr[end+1]-= 1
            else:
                arr[start] -= 1
                arr[end+1]+= 1
        for i in range(1,len(arr)):
            arr[i]+= arr[i-1]
        arr.pop()

        for ind,shift in enumerate(arr):
            code = ord(res[ind]) - 97  
            shifted = (code + shift) % 26      
            res[ind] = chr(shifted + 97)

        return "".join(res)
        