class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l= i+1
            r= len(nums)-1
            while l < r:
                threesum= nums[i] + nums[l]+nums[r]
                if threesum == 0:
                    res.append([nums[i] , nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif threesum >0:
                    r-=1
                else:
                    l+=1
        return res


        