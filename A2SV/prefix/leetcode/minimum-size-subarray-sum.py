class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        length = len(nums) + 1  
        _sum = 0  

        while right < len(nums):
            _sum += nums[right]
            right += 1

            while _sum >= target:
                length = min(length, right - left)
                _sum -= nums[left]
                left += 1

        return 0 if length == len(nums) + 1 else length
        