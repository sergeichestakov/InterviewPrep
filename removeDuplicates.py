class Solution:
    def removeDuplicates(self, nums):
        """
        Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(set(nums))
        return len(nums)
