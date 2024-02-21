class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = 0 
        myarray=[]
        res = 0
        for i in costs:
            total+= i[0]
            myarray.append(i[1]- i[0])
        myarray.sort()
        n = int(len(myarray)/2)
      
        for i in range(n):
            res+= myarray[i]

        return res + total
        