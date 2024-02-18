class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        oper=["/","+","-","*"]
        i=0
        while i < len(tokens):
            if tokens[i] not in oper:
                stack.append(int(tokens[i]))
                i += 1
            else:
                nums2 = stack.pop()
                nums1 = stack.pop()
                if tokens[i] == "*":
                    total = nums1 * nums2
                elif tokens[i] == "+":
                    total = nums1 + nums2
                elif tokens[i] == "-":
                    total = nums1 - nums2
                elif tokens[i] == "/":
                    total = int(nums1 / nums2)
                   

                stack.append(total)
            
                i += 1
           

        return stack[0]