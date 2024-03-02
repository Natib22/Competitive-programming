class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        Mod = 10 ** 9 + 7
        freq = [0] * (len(nums) +1)
        ans = 0
        for i,j in requests:
            freq[i] +=1
            freq[j+1] += -1
        for i in range(1,len(freq)):
            freq[i] +=freq[i-1]
        nums.sort(reverse = True)
        freq.sort(reverse = True)
        for ind ,val in enumerate(freq):
            if val == 0 :
                break
            ans += val * nums[ind]
        return ans % Mod
        