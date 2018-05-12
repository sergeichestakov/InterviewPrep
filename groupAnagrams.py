# Given an array of strings, group anagrams together.
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = {}
        for string in strs:
            key = tuple(sorted(string))
            if key not in ret:
                ret[key] = []
            ret[key].append(string)

        return list(ret.values())
