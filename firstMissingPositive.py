# Given an unsorted integer array, find the smallest missing positive integer.
# Your algorithm should run in O(n) time and uses constant extra space.
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
	#Iterate through array and rearrange such that each number is placed in nums[num - 1]
        length = len(nums)
        for index in range(length):
            target = nums[index]
            while target > 0 and target <= length and target != nums[target - 1]:
                temp = nums[target - 1]
                nums[target - 1] = target
                target = temp

	#Find first number that is out of place, otherwise return length + 1
        for index in range(length):
            if index + 1 != nums[index]:
                return index + 1

        return length + 1
