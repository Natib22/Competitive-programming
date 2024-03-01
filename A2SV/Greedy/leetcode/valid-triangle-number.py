class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums)-1,1 ,-1):
            left = 0
            right = i -1
           
            while left < right:
               
                if nums[right] + nums[left] > nums[i]:
                    ans += right - left
                    right-=1
                else:
                    left+=1
        return ans
        