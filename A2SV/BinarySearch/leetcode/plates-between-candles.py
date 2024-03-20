from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        pref = [0]  
        candles = []
        ans = []
        curr = 0
        for ind, i in enumerate(s):
            if i == "*":
                curr += 1
            else:
                candles.append(ind)
            pref.append(curr)

        def searchfirst(num):
            left, right = -1, len(candles)
            while right - left > 1:
                mid = (right + left) // 2
                if candles[mid] >= num:
                    right = mid
                else:
                    left = mid
            return candles[right] if right < len(candles) else float('inf')

        def searchlast(end):
            left, right = -1, len(candles)
            while right - left > 1:
                mid = (right + left) // 2
                if candles[mid] <= end:
                    left = mid
                else:
                    right = mid
            return candles[left] if left >= 0 else -1

        for i in queries:
            start, end = searchfirst(i[0]), searchlast(i[1])
            if start != float('inf') and end != -1 and start <= end:
                ans.append(pref[end + 1] - pref[start])
            else:
                ans.append(0)

        return ans

        