class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans= [-1] * len(nums1)
        mymap = {}
        stack = []
        for i,j in  enumerate(nums1):
            mymap[j] = i
      
        for i in nums2:
            if not stack:
                stack.append(i)
            else:
                while  stack and i > stack[-1] :
                    
                    if stack[-1] in mymap:
                        ans[mymap[stack[-1]]] = i
                    stack.pop()
                stack.append(i)
                    

        return ans 

        