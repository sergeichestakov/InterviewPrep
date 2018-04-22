class Solution:
    def twoSum(self, nums, target):
        """
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        dict = {}
        for index, entry in enumerate(nums):
            complement = target - entry
            if complement in dict:
                ret.extend((dict[complement], index))
            dict[entry] = index
        return ret
