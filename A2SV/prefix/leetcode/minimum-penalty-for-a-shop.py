class Solution:
    def bestClosingTime(self, customers: str) -> int:
        yes=[0] * (len(customers)+1)
        no=[0] * (len(customers)+1)
        sum=0
        for i in range(len(customers)-1,-1,-1):
            if customers[i]=="Y":
                sum+=1
            yes[i]=sum
            
        sum=0
        for i in range(len(customers)):
            if customers[i]== "N":
                sum+=1
            no[i+1]=sum
        res = len(yes)
        summ= len(yes)
        print(yes, no)
        for i in range(len(yes)):
            if summ > yes[i] + no[i]:
                res=i
                summ= yes[i]+ no[i]
        return res




 
        
        