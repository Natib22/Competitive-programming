class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0:
            return target - 1
        
        
        counter =0 
        while target > 1:
            if maxDoubles > 0  and target % 2 == 0:
                target = target // 2
                maxDoubles-=1
                counter+=1
            elif maxDoubles == 0 :
                return counter + target -1
            else:
                counter +=1
                target-=1
          
        return counter

        