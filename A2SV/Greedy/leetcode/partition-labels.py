class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mymap ={}
        for ind ,char in enumerate(s):
            mymap[char] = ind
        
        res = []
        start = end = 0
        curr = 0
        for ind,char in enumerate(s):
            curr = max(curr , mymap[char])
            if ind < curr:
                end+=1
            else:
                res.append(end- start +1)
                start = end

        return res

   
        
        