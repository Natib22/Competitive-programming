class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        low = float('inf')
        mid = float('inf')
        for i in nums:
            if i <= low:
                low = i
            elif i <=mid:
                mid = i
            else:
                return True
        return False
                

        