class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left , right = 0 , len(arr)-1
        curr = -1
        ans = []

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                curr = mid
                break
            elif arr[mid] > x:
                right = mid-1
            else:
                left = mid +1
        if len(arr) == k:
            return arr
        if curr!= -1:
            left ,right = curr , curr  + 1
        else:
            right = left
            left-=1
        while k > 0:
          
            if right >= len(arr) or( left > -1 and abs(arr[left] - x) <= abs(arr[right] - x)):
                ans.append(arr[left])
                left-=1
            elif left < 0  or( right < len(arr) and abs(arr[right] - x) < abs(arr[left] - x)):
                ans.append(arr[right])
                right+=1
            k-=1
        ans.sort()
        return ans