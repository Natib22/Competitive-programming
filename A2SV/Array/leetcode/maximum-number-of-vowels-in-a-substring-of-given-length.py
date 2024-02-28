class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        myset=set(['a','e','i','o','u'])
        vowels = 0
        left = right = 0
        ans = 0
        while right < len(s):
            if right - left  < k:
                if s[right] in myset : 
                    vowels+=1
                right+=1
                
            else:
                if s[right] in myset:
                    vowels+=1
                if s[left] in myset:
                    vowels-=1
                left+=1
                right+=1
            ans = max(vowels  , ans)
        return ans



        