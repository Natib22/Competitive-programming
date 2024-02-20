class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
            if k == 1:
                return max(nums)

            sum_val = sum(nums[:k])
            max_sum = sum_val

            for i in range(len(nums) - k):
                sum_val += nums[i + k] - nums[i]
                max_sum = max(max_sum, sum_val)

            return max_sum / k
                