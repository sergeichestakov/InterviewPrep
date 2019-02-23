# We are given two arrays A and B of words.  Each word is a string of lowercase letters.
# Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".
# Now say a word a from A is universal if for every b in B, b is a subset of a.
# Return a list of all universal words in A.  You can return the words in any order
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans
        
        bMax = [0] * 26
        for b in B:
            for index, char_count in enumerate(count(b)):
                bMax[index] = max(bMax[index], char_count)
                
        ans = []
        for a in A:
            a_count = count(a)
            all_subset = True
            for index in range(len(a_count)):
                if a_count[index] < bMax[index]:
                    all_subset = False
                    break
                    
            if all_subset:
                ans.append(a)
                
        return ans
