class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans = 0
        num = 0
        count = 0
        for i in flips:
            num = max(i , num)
            count+=1
            if count == num:
                ans+=1
        return ans
        