class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        mymap = defaultdict(int)
        myset = set(nums)
        distinct = len(myset)
        ans = left =0
        for right in range(len(nums)):
            mymap[nums[right]]+=1
            while len(mymap) == distinct and left <= right:

                ans+=1 
                ans+= len(nums)-right -1
                mymap[nums[left]]-=1
                if mymap[nums[left]] == 0:
                    mymap.pop(nums[left])
                left+=1
        return ans
        