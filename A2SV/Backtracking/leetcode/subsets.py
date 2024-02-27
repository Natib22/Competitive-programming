class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]
        def my(j,path):
            if j >= len(nums) :
                return
            
            for i in range(j , len(nums)):
                path.append(nums[i])
                my(i+1,path)
                arr.append(path[:])
                path.pop()
        my(0,[])
        return arr

        