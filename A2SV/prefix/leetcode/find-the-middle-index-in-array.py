class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pref=[0]*len(nums)
        suff=[0] * len(nums)
        total=0
        for i in range(len(nums) - 2, -1, -1):
            total += nums[i + 1]
            suff[i] = total
        total=0
        for i in range(1, len(nums)):
            total+= nums[i - 1]
            pref[i] = total
           
            
        for i in range(len(nums)):
            if pref[i]==suff[i]:
                return i


        return -1


        