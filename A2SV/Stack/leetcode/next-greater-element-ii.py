class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        myarray=[-1]*length
        stack=[]
        for i in range(length * 2):
            index= i % length
            while stack and nums[index] > nums[stack[len(stack)-1]]:
                poped=stack.pop()
                myarray[poped]= nums[index]
            if i<length:
                stack.append(i)
        
        return myarray


       