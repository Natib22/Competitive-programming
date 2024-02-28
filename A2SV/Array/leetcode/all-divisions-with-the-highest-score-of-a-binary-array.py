class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        arr = [0] * (len(nums) + 1)
        ones = zeros = 0
        res = []
        ones = sum(nums)
        
        for ind ,i in enumerate(nums):
            arr[ind] = zeros + ones
            if i == 0:
                zeros+=1
            else:
                ones-=1
        arr[-1] = zeros

        for ind ,i in enumerate(arr):
            if not res or i > arr [res[-1]]:
              
                print(res)
                res = []
                res.append(ind)
            elif i == arr [res[-1]]:
                res.append(ind)
        return res
