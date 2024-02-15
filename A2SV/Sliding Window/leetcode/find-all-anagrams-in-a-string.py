class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        pCount= {}
        currentmap={}
        myarray=[]
        for i in range(len(p)):
            pCount[p[i]] = pCount.get(p[i],0)+1
        if len(p)> len(s):
            return myarray
        
        for i in range(len(p)):
            currentmap[s[i]] = currentmap.get(s[i],0)+1
        
        l=0
        r= len(p)-1
        while r < len(s):
            if currentmap== pCount:
                myarray.append(l)
            
            currentmap[s[l]]-=1
            if currentmap[s[l]]==0:
                currentmap.pop(s[l])
            l+=1
            r+=1
            if r < len(s):
                currentmap[s[r]]= 1+ currentmap.get(s[r],0)

        return myarray