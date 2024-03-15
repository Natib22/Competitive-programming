class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        mymax = max(nums)
        left , right = 0, mymax+1
        ans = mymax
        while right - left > 1:
            mid = (right + left) // 2
            temp = 0
            for i in nums:
                temp += math.ceil(i / mid)
            if temp <= threshold:
                right = mid
            else:
                left = mid
        return right