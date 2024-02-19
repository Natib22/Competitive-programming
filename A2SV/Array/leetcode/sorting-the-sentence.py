class Solution:
    def sortSentence(self, s: str) -> str:
        myarray = s.split()
        res = []
        for i in myarray:
            res.append([i[-1],i[:-1]])
        res.sort()
        string = ""
        string+=res[0][1]
        for i in range(1,len(res)):
            string+= " "+res[i][1]
        return string

        