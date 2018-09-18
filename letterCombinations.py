# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution:
    letters = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if digits: # Generate combs of nonempty string
            self.makeCombs(digits, '', res)
        return res

    def makeCombs(self, digits, curr, res):
        if not digits: # Empty string so append current comb to return array
            res.append(curr[:])
        else: # Recursively generate remaining combs
            first = int(digits[0])
            for letter in Solution.letters[first]:
                self.makeCombs(digits[1:], curr + letter, res)
