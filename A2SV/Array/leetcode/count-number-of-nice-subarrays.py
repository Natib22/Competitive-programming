class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans= odds = 0
        mymap = {0:1} 
        arr = [0] * len(nums)

        for ind , val in enumerate(nums):
            if val%2 == 1:
                arr[ind] = 1
        total =0
       
        for i in range(len(arr)):
            total+=arr[i]
            if total - k in mymap:
                ans+=mymap[total - k] 
            mymap[total] = mymap.get(total ,0)+1

        return ans