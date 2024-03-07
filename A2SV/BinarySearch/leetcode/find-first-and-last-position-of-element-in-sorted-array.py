class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left , right = 0, len(nums)-1
        ans= [-1,-1]
        while left <= right:

            mid = (left + right) //2
            if nums[mid] == target:
                right = left = mid
                ans = [left,right]
                left-=1
                right+=1
              
                while left >=0 and nums[left] == target :
                    left-=1
                    ans[0]-=1
                while right <len(nums) and nums[right] == target :
                    right+=1
                    ans[1]+=1
                
                return ans

            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid+1
        return ans
                 
        
        