class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left , right = 0 , len(skill)-1
        ans=0
        myset = {skill[right] + skill[left]}
   
        while left < right:
            n = skill[right] * skill[left]
            if skill[right] + skill[left] not in myset:
                return -1
            ans+= n
            right-=1
            left+=1
        
            
        return ans

        