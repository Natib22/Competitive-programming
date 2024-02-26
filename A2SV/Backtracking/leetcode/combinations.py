class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        arr = []
        def my(num,path):
            if len(path) == k :
                arr.append(path[:])
                return
            for i in range(num , n+1):
                path.append(i)
                my(i+1,path)
                path.pop()
        my(1,[])
        return arr
