# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
# If possible, output any possible result. If not possible, return the empty string.
class Solution:
    def reorganizeString(self, S: str) -> str:
        length = len(S)
        sortedArr = []
        counts = [(S.count(char), char) for char in set(S)]
        for count, char in sorted(counts):
            if count > (length + 1)/2:
                return ""
            else:
                sortedArr.extend(count * char)
                
        ans = [None] * length
        ans[::2], ans[1::2] = sortedArr[length//2:], sortedArr[:length//2]
        return "".join(ans)
