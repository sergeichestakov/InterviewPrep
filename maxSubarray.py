# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Start with first element
        currSum = maxSum = nums[0]

        # Iterate through array and update current and maximum sum seen so far
        for num in nums[1:]:
            currSum = max(currSum + num, num)
            maxSum = max(maxSum, currSum)

        return maxSum
