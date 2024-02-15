class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        counter = 0
        greed = sorted(g)
        cookie = sorted(s)
        
        i, j = 0, 0
        
        while i < len(greed) and j < len(cookie):
            if greed[i] <= cookie[j]:
                counter += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return counter
