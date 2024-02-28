class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        def my(path):
            if len(path) == len(nums):
                arr.append(path[:])
            
            for i in nums:
                if i not in path:
                    path.append(i)
                    my(path)
                    path.pop()
        my([])
        return arr


        