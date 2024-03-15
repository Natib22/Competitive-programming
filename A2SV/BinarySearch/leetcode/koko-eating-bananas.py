class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        left , right = 0 , total
        while right  - left > 1:
            mid = (left + right) // 2
            counter = 0
            for i in piles:
                counter+= math.ceil(i/mid)

            if counter > h:
                left = mid
            else:
                right = mid
        return right
        