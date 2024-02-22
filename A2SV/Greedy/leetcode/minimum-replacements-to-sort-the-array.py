class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        curr = nums[-1]
        res =0 
        if len(nums) <=1:
            return 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > curr:
                step = ((nums[i]-1 )// curr) 
    
                res+=step
                curr = nums[i] // (step+1)

            else:
                curr = nums[i]
        return res

        