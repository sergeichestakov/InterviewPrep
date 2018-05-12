# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        self.generate(ret, [], n, k, 1)
        return ret

    def generate(self, ret, temp, n, k, start):
        if k == 0:
            ret.append(temp[:])
        else:
            for num in range(start, n - k + 2):
                temp.append(num)
                self.generate(ret, temp, n, k - 1, num + 1)
                del temp[-1]
