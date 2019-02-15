# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s.
# If there isn't one, return 0 instead.
class Solution:
    def minSubArrayLen(self, s: 'int', nums: 'List[int]') -> 'int':
        length = len(nums)
        minLen = sys.maxsize
        left, sum = 0, 0
        for index in range(length):
            sum += nums[index]
            while sum >= s:
                minLen = min(minLen, index + 1 - left)
                sum -= nums[left]
                left += 1
        
        return minLen if minLen != sys.maxsize else 0
