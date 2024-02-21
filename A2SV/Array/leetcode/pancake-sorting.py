class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        curr = len(arr) -1
        for i in range(len(arr)-1,0,-1):
            mymax = i
            for j in range(i-1 , -1, -1):
                if arr[j] > arr[mymax]:
                    mymax = j
            if mymax != i:
                self.flip(arr , 0 , mymax)
                self.flip(arr , 0 , curr)
                res .append(mymax+1)
                res.append(curr+1)
            curr-=1
      

        return res


    



    def flip(self,array,start,end):
        while start< end:
            [array[start],array[end]]= [array[end],array[start]]
            start+=1
            end-=1


        