class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        pt = len(processorTime) 
        t = len(tasks)
        res = 0
        left , right =  0 , t-1
        
        while left <  pt and right > 0:
            res = max(res , processorTime[left] + tasks[right])
            right -= 4
            left+=1
        return res
        