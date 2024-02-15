class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x : x[1])
        stack = []
        ans = 0
        for i in points:
            if not stack:
                stack.append(i)
            else:
                if stack[-1][1] >= i[0]:
                    continue
                else:
                    ans+=1
                    stack.pop()
                    stack.append(i)
      
     
        return ans+ len(stack)
        