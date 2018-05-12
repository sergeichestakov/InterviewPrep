# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ret = []
        self.generatePartitions(ret, [], s, 0)
        return ret

    def generatePartitions(self, ret, tempList, s, start):
        if start == len(s):
            ret.append(tempList[:])
        else:
            for index in range(start, len(s)):
                if self.isPalindrome(s, start, index):
                    tempList.append(s[start:index + 1])
                    self.generatePartitions(ret, tempList, s, index + 1)
                    del tempList[-1]

    def isPalindrome(self, s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True
