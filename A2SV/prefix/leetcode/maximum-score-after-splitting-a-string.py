class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones=[0] * len(s)
        zero=[0] * len(s)
        cum=0
        res=0
        for i in range(len(s)-1,0,-1):
            if s[i]=="1":
                cum+=1
            ones[i]= cum
        cum=0
        for i in range(len(s)-1):
            if s[i]=="0":
                cum+=1
            zero[i+1]= cum
        for i in range(len(s)):
            res= max(res, zero[i]+ ones[i] )
        print(ones,zero)
        return res
        
        

            

        