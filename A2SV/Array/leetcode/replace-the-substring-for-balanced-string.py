class Solution:
    def balancedString(self, s: str) -> int:
        mymap = defaultdict(int)
        N = len(s)
        for i in s:
            mymap[i]+=1
        ans = len(s) + 1
        left = 0
        target = len(s)//4
        
        if mymap["W"] == target and mymap["E"] == target and mymap["Q"] == target and mymap["R"] == target:
            return 0

        for right in range(len(s)):
            mymap[s[right]]-=1
            while left <= right and mymap["W"] <= target and mymap["E"] <= target and mymap["Q"] <= target and mymap["R"] <= target:
               
                ans = min(ans,right - left +1)
                mymap[s[left]] +=1
                left+=1
        return ans
        