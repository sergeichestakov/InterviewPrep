# Suppose Andy and Doris want to choose a restaurant for dinner, 
# and they both have a list of favorite restaurants represented by strings.
# You need to help them find out their common interest with the least list index sum. 
# If there is a choice tie between answers, output all of them with no order requirement. 
# You could assume there always exists an answer.
class Solution:
    def findRestaurant(self, list1: 'List[str]', list2: 'List[str]') -> 'List[str]':
        indices = {}
        res = []
        for index, word in enumerate(list1):
            indices[word] = index
            
        minSum = sys.maxsize
        
        for index, word in enumerate(list2):
            if word in indices:
                sum = index + indices[word]
                if sum < minSum:
                    res = [word]
                    minSum = sum
                elif sum == minSum:
                    res.append(word)
                    
        return res
