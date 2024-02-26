class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = []
        candidates.sort()
        def my(j , path):
            if sum(path) == target:
                arr.append(path[:])
            elif sum(path) > target:
                return
            
            for i in range(j,len(candidates)):
                path.append(candidates[i])
                my(i,path)
                path.pop()
        
        my(0,[])
        return arr

        