class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0
        left=0
        right=0
        while right < len(s) and left <len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            
            while (right-left+1)-max(count.values())> k:
             
                count[s[left]]-=1
                left+=1
            right+=1
            res= max(res, right-left)
        return res
        