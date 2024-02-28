class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        bal  = 0
        for ind , ch in enumerate(s):
            if ch == "(":
                bal+=1
            else:
                bal-=1
                if s[ind-1] == "(":
                    score+= 2**bal
        return score
        