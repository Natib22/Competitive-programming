class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        myarray = [0]* len(nums)
        nums.sort()
        tracker = 0
        res = 0
        if len(nums) ==1:
            return 0
        for i in range(1 , len(nums)):
            if nums[i] > nums[i-1]:
                tracker+=1
            myarray[i]+=tracker
            res+=myarray[i]
            
        return res
        