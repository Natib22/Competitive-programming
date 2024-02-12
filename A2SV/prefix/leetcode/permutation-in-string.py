class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map={}
        currentmap={}
        if len(s1) > len (s2):
            return False
  
        for i in s1:
            s1map[i]= 1+ s1map.get(i,0)
        for i in range(len(s1)):
            currentmap[s2[i]]= 1+ currentmap.get(s2[i],0)
        left=0
        right= len(s1)-1
        
        while right < len(s2):
            if currentmap == s1map:
                return True
               
            if s2[left] in currentmap:
                currentmap[s2[left]] -= 1
            if currentmap[s2[left]]==0:
                currentmap.pop(s2[left])
            left+=1
            right+=1
            if right < len(s2):
                currentmap[s2[right]]=1+ currentmap.get(s2[right],0)
  
        return False
        