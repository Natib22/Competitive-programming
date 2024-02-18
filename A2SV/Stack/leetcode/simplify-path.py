class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack= []
        myarray= path.split('/')
        for ch in myarray:
            if(ch=="" or ch=="."):
                continue
            elif ch=="..":
                if len(stack) !=0:
                    stack.pop()
             
            else:
                stack.append(ch)
        return "/" + "/".join(stack)

             
        