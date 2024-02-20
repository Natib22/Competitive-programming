class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = ones = zeroes =left =right = 0 
         
        if k == 0:
            temp = 0
            for i in nums:
                if i:
                    temp+=1
                    ans = max(temp , ans)
                else:
                    temp = 0
            return ans

        while right < len(nums):
            if nums[right] == 1:
                ones+=1
            else:
                zeroes+=1
            while left < right and (right - left +1) - ones > k:
                if nums[left] == 1:
                    ones-=1
                else:
                    zeroes-=1
                left+=1
            ans = max(ans , right - left+1)
            right+=1
            
        return ans

        