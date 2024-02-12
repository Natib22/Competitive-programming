class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        myarray=[0] * 1001
        for num, start, end in trips:
            myarray[start]+= num
            myarray[end]+= - num
        
        for i in range(1,len(myarray)):
            myarray[i]+= myarray[i-1]
        
        for i in myarray:
            if i > capacity:
                return False

   
        return True

        
        