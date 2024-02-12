class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        count = 0
        sum_dict = {0: 1}
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum - goal in sum_dict:
                count += sum_dict[current_sum - goal]
            sum_dict[current_sum] = sum_dict.get(current_sum, 0) + 1
        print(sum_dict)
        return count