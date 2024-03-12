class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        mod = 10**9 + 7
        print(nums)
        for ind, val in enumerate(nums):
            if val * 2 > target:
                break  
            temp = self.binary(target - val, nums)
            ans += pow(2, temp - ind)   
        return ans % mod
            
            
    def binary(self, target, nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right
        