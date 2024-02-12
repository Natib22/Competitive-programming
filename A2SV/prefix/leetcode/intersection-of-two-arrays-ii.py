class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        myarray= []
        l=0
        r=0
        nums1.sort()
        nums2.sort()

        while(l<len(nums1) and r< len(nums2)):
            if nums1[l]==nums2[r]:
                myarray.append(nums1[l])
                l+=1
                r+=1
            elif nums1[l]<nums2[r]:
                l+=1
            else:
                r+=1
        return myarray
              

        