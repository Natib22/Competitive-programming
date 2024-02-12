class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sum_dict = {0: 1}
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum - k in sum_dict:
                count += sum_dict[current_sum - k]
            sum_dict[current_sum] = sum_dict.get(current_sum, 0) + 1

        return count

        