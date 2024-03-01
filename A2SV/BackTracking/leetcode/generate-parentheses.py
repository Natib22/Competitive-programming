class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        arr = []
        brack = "(" *n
        def my(path):
            if len(path) == 2 * n:
                dummy = "".join(path)
                if self.isValid(dummy):
                    arr.append(dummy)
                return
            
            
            path.append('(')
            my(path)
            path.pop()
            path.append(')')
            my(path)
            path.pop()
                
        my([])
        return arr
        
    def isValid(self, s):
        mymap = { "}":"{",  ")":"(", "]":"[" }
        myset = {"{", "(", "["}
        stack = []
        for i in s:
            if i in myset :
                stack.append(i)
            
            else:
                if not stack :
                    return False
                elif stack.pop() != mymap[i]:
                    return False
        
        return len(stack) == 0
        