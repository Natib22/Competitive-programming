class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        modarr={0:1}
        count=0
        prefix=0
        for i in nums:
            prefix+=i
            if (prefix +k)%k in modarr:
                count+=modarr.get(prefix%k)
            modarr[prefix%k]= modarr.get(prefix%k,0)+1
        return count

        