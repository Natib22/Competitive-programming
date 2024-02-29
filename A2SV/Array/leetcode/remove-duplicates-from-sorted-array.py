class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left ,right = 1 ,1
        curr = nums[0]
        while right < len(nums):
            
            if nums[right] > curr:
                nums[left] = nums[right]
                left+=1
                curr = nums[right]
           
            right+=1
            
            
        return left

        