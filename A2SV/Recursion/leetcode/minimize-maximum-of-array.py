class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = total = nums[0]
        for i in range(1,len(nums)):
            total+= nums[i]
            temp = math.ceil(total / (i + 1))
            
           
            ans = max(ans , temp)
        return ans
        
        