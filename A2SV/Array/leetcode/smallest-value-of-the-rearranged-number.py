class Solution:
    def smallestNumber(self, num: int) -> int: 
        arr = []
        flag = num > 0
        i = 0 if flag else 1
        num= str(num)
        if len(num) <=1:
            return int(num)

        for j in range(i,len(num)):
            arr.append(num[j])

        if flag:
            arr.sort(key = lambda x : int(x))
            if arr[0] == "0":
                i = 0 
                for ind, x in enumerate(arr):
                    if x != "0":
                        i = ind
                        break
                [arr[0] , arr[i]] = [arr[i] , arr[0]]

        else:
            arr.sort(key = lambda x : int(x), reverse = True)
            return int("".join(arr)) * -1
        
        return int("".join(arr))
        
        