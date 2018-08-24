# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False
