class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mymap = defaultdict(int)
        left = right = ans = total = 0
        while right < len(nums):
            total+= nums[right]
            mymap[nums[right]]+=1

            while len(mymap) < right - left +1:
                mymap[nums[left]]-=1
                total-=nums[left]
                if mymap[nums[left]] == 0:
                    mymap.pop(nums[left])
                left+=1
            
      

            ans = max(ans , total)
            right+=1

        return ans


        