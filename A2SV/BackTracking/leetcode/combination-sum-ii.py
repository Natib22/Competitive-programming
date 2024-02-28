class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = []
        myset = set()
        tot=[0]
        candidates.sort()
        if sum(candidates) < target:
            return []
        def my(j , path):
            if tot[0] == target:
                dummy = tuple(path)

                if dummy not in myset:
                    arr.append(list(dummy))
                myset.add(dummy)
            elif tot[0] > target:
                return
            for ind in range(j, len(candidates)):
                if ind > j and candidates[ind] == candidates[ind - 1]:
                        continue
                path.append(candidates[ind])
                tot[0] += candidates[ind]
                if tot[0]<=target:
                    my(ind + 1,path)
                tot[0]-= candidates[ind]
                path.pop()
        my(0,[])
        return arr
        

        
        

        