class Solution:
    def generate(self, nums, curr, ret):
        if(len(nums) == 0):
            ret.append(curr)
            return
        else:
            for index in range(len(nums)): #Swap each index and permute
                nums[0], nums[index] = nums[index], nums[0]
                self.generate(nums[1:], curr + [nums[0]], ret)

    # Given a collection of distinct integers, return all possible permutations.
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.generate(nums, [], ret)
        return ret
