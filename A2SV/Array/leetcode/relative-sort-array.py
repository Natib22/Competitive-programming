class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        temp = []
        mymap = Counter(arr1)
        myset = set(arr2)
        
        for i in arr2:
            res+=[i]*mymap[i] 
        for key , val in mymap.items():
            if key not in myset:
               temp+=[key]* val
        return res + sorted(temp)
        
        