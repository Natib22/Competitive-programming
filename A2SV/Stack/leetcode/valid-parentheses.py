class Solution:
    def isValid(self, s: str) -> bool:
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
                    



        