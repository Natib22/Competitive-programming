class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left , right = max(weights) , sum(weights)
        ans = sum(weights)
        while left <= right:
            mid = (left + right) // 2
            counter=0
            curr = 0
            for i in weights:
               
                if curr + i > mid:
                    counter+=1
                    curr = 0
                curr+=i
            print(counter)
            counter+=1
            if counter > days:
                left = mid+1
            else:
                ans  = min(mid , ans)
                right = mid-1
        return ans
                
            






        