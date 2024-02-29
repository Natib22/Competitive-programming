class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        myarray = []
        if nums == [0] * len(nums):
            return "0"
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        def compare(i , j):
            if i + j > j + i:
                return -1
            elif i + j < j + i:
                return 1
            else:
                return 0
        nums.sort(key=cmp_to_key(compare))
      
       
        return "".join(nums)

        
        
        