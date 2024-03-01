class Solution:
    def longestPalindrome(self, s: str) -> int:
        mymap = defaultdict(int)
        for i in s:
            mymap[i] +=1
        ans = 0
        flag = False
        print(mymap)
        for key , val in mymap.items():
            if val % 2 == 0:
                ans+= val
            else:
                flag = True
                ans+= val -1
        return ans+1 if flag else ans
        