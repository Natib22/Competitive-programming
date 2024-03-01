class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        suff = [0] * N
        pref = [0] * N
        absolute =[0] * N
        tracker = tracker2 = 0
        total = sum(nums)

        for ind , val in enumerate(nums):
            tracker+= val
            tracker2+= nums[N-1-ind]
            suff[ind] = total - tracker
            pref[N-1-ind]= total - tracker2
        
        for ind , val in enumerate(nums):
            absolute[ind]=((val*ind)-pref[ind])+(suff[ind]-(val*(N-ind-1)))
        
        return absolute

        
    

        