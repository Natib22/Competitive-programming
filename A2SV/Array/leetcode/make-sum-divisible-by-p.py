class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0
        
        runningSum = 0
        mymap = {0: -1}
        min_len = len(nums)
        current = 0
        
        for i, num in enumerate(nums):
            runningSum = (runningSum + num) % p
            current = (runningSum - target) % p
            
            if current in mymap:
                min_len = min(min_len, i - mymap[current])
            
            mymap[runningSum] = i
        if min_len < len(nums):
            return min_len 
        
        return  -1



        




        