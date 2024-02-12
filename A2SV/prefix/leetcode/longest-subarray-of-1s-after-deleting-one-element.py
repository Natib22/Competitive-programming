class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        zeroes = 0
        left = 0
        right = 0
        ans = 0

        while right < len(nums) and left < len(nums):
            if nums[right] == 0:
                zeroes += 1
            else:
                ones += 1
          
            while right < len(nums) and zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                else:
                    ones -= 1
                left += 1

            right += 1
            ans = max(ans, zeroes + ones)

        return ans-1



        