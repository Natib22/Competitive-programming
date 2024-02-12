class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest= 1e8
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l <r:
                threesum = nums[i]+nums[r]+nums[l]
                if abs(threesum - target) < abs(closest - target):
                    closest = threesum
                if threesum == target:
                    return target
                elif threesum > target:
                    r-=1
                else :
                    l+=1
        return closest
        