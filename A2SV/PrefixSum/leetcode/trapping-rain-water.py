class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        right = [0]* len(height)
        left  = [0] * len(height)
        curr = 0
        
        for ind, val in enumerate(height):
            left[ind] = curr
            curr = max(curr , val)
        curr = 0

        for i in range(len(height)-1,-1,-1):
            right[i] = curr
            curr = max(curr,height[i])

        for ind, val in enumerate(right):
            h = min(val , left[ind])
            if h - height[ind]>0:
                water+= h - height[ind]
        return water

            




        