class Solution(object):
    def maxSubArray(self, nums):
        curr_sum = 0
        max_sum = float('-inf')


        for num in nums:

            curr_sum += num
            max_sum = max(curr_sum, max_sum)

            if curr_sum < 0:
                curr_sum = 0
        

        return max_sum


        