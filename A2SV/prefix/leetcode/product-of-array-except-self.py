class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        
        calc = 1
        for i in range(1, len(nums)):
            calc *= nums[i - 1]
            prefix[i] = calc

   
        calc = 1
        for i in range(len(nums) - 2, -1, -1):
            calc *= nums[i + 1]
            suffix[i] = calc

        for i in range(len(nums)):
            suffix[i] *= prefix[i]

        return suffix



        
        