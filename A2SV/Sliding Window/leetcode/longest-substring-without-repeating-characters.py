class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        myset = set ()
        left=0
        right=0
        length=0
        while right < len(s):
            if s[right] not in myset:
                myset.add(s[right])
                length= max(length,len(myset))
                right+=1
            elif s[right] in myset:
                myset.remove(s[left])
                left+=1
                
        return length

        