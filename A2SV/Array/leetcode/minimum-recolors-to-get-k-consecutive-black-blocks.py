class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0
        left = right = 0
        ans = k
        while right < len(blocks):
            while right - left +1 < k:
                if blocks[right] == "W":
                    whites+=1
                right+=1
            
            
            if blocks[right] == "W":
                whites+=1
            ans = min(ans ,whites)
            if blocks[left] == "W":
                whites-=1
            right+=1
            left+=1
        return ans
        