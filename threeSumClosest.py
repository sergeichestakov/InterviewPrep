# Given an array nums of n integers and an integer target, 
# find three integers in nums such that the sum is closest to target. 
# Return the sum of the three integers. 
# You may assume that each input would have exactly one solution
class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        closest, minDiff = 0, sys.maxsize
        nums.sort()
        for index in range(len(nums) - 2):
            if index > 0 and nums[index] == nums[index - 1]: # Avoid duplicates
                continue
            left = index + 1 # Maintain two pointers
            right = len(nums) - 1
            while left < right:
                sum = nums[index] + nums[left] + nums[right]
                diff = abs(sum - target)
                if diff < minDiff:
                    closest = sum
                    minDiff = diff
                if sum < target:
                    left += 1
                else:
                    right -= 1
                        
        return closest
