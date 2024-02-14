class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        runningSum = 0
        patch = i = 0
        dummy = 1
     
        
        while i < len(nums) and runningSum <= n:
            if runningSum + 1 >= nums[i]:
               
                dummy += 1
            else:
                while runningSum < nums[i] and runningSum <= n:
                    if runningSum >= dummy:
                        dummy += 1
                    elif dummy == nums[i]:
                        break

                    else:
                        
                        patch += 1
                        print(dummy)
                        runningSum += dummy
                        dummy += 1
            runningSum += nums[i]
            i += 1
        
        while runningSum < n:
            patch += 1
            runningSum += runningSum + 1
        
        return patch


     

    



        