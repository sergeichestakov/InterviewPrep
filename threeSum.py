#Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        for index in range(len(nums) - 2):
            if index > 0 and nums[index] == nums[index - 1]: #Avoid duplicates
                continue
            left = index + 1 #Maintain two pointers
            right = len(nums) - 1
            while left < right:
                sum = nums[index] + nums[left] + nums[right]
                if sum < 0: #Advance according to sum because array is sorted
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    ans = [nums[index], nums[left], nums[right]]
                    ret.append(ans)
                    if left < right: #Advance indices until found a new number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return ret
