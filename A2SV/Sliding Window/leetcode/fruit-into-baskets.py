class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mymap={}
        count=0
        left=0
        right=0
        while right < len(fruits):
            mymap[fruits[right]]= 1+ mymap.get(fruits[right],0)
                
            while left <right  and len(mymap) > 2:
                mymap[fruits[left]]-=1
                if mymap[fruits[left]]==0:
                    mymap.pop(fruits[left])
                left+=1

            
            count= max ( count, right-left +1)

            right+=1
        return count
        