# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(n):
            if n==1:
                return ["()"]
            else:
                strSet = set()
                for res in generate(n-1):
                    for index in range(len(res)):
                        strSet.add(res[:index] + "()" + res[index:])
                return list(strSet)

        return generate(n)
