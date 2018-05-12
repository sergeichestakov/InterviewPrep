# Write a function that takes a list L and returns a random sublist of size N of that list.
# Assume that the indices must be in increasing order, meaning you cannot go backwards.
import random

class Solution:
    def randomSublist(self, arr, N):
        res = []
        self.generate(arr, res, [], N, N)
        randIndex = random.randint(0, len(res) - 1)
        return res[randIndex] #Return a random sublist

    #Generate the sublists recursively
    def generate(self, arr, res, temp, N, remain):
        if(len(temp) == N):
            res.append(temp[:])
        else:
            for index in range(len(arr) - remain + 1):
                temp.append(arr[index])
                self.generate(arr[index + 1:], res, temp, N, remain - 1)
                del temp[-1]
