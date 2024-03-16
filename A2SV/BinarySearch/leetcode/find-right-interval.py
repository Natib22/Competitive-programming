class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = []
        starts = []
        for i in range(len(intervals)):
            starts.append([intervals[i][0] , i])
        starts.sort()
   
        def search(num):
            left , right = -1 , len(starts)
            while right - left > 1:
                mid = (right + left) // 2
                if starts[mid][0] == num:
                    return mid
                elif starts[mid][0] < num:
                    left = mid
                else:
                    right = mid
            return right
        for start , end in intervals:
            curr = search(end)
            if curr == len(starts):     
                ans.append(-1)
            else:
                ans.append(starts[curr][1])
        return ans

        