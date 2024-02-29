class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left , right = 0 , 0
        ans = []
        while left < len(firstList) and right < len(secondList):
            start = max(firstList[left][0], secondList[right][0])

            end = min(firstList[left][1], secondList[right][1])
            if start <= end:
                ans.append([start,end])
            if firstList[left][1] < secondList[right][1]:
                left+=1
            else:
                right+=1
        return ans
