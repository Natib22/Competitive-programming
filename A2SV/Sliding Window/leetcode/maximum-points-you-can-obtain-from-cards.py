class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total=0
        res=0
        left=0 
        right=0
        arrSum=sum(cardPoints)
        print(arrSum)
        if k == len(cardPoints):
            return arrSum
        num=len(cardPoints)-k
        for right in range(num):
            total+=cardPoints[right]
        res= arrSum-total
      
        while right < len(cardPoints)-1:
           
            right+=1
            total+=cardPoints[right]
            total-=cardPoints[left]
            left+=1
          
            res= max(res,arrSum-total)
        return res
        