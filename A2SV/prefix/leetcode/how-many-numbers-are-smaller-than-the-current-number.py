class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)  
        myarray = []
        for i in range(len(nums)):
            myarray.append(sorted_nums.index(nums[i]))  
        return myarray
