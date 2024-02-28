class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left , right = 0 , len(nums) -1
        k = 0
        for i in nums:
            if i != val:
                k+=1
        while left < k:
            if nums[left] == val and nums[right] != val:
                [nums[left] , nums[right]] = [nums[right],nums[left]] 
            elif nums[right] == val:
                right-=1
            else:
                left+=1
        return k
        