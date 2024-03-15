class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left , right = max(nums)-1 , sum(nums) +1
        while right -left >1:
            mid = (left + right) // 2
            curr = 0
            sect = 0
            for i in nums:
                if curr + i > mid:
                    sect+=1
                    curr = 0
                curr += i
            sect +=1
            if sect > k :
                left = mid
            else:
                right = mid
        return right
        