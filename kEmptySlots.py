# There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days.
# In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.
# Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.
# For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.
# Given an integer k, you need to output in which day there exists two flowers in the status of blooming, and there are k flowers between them that are not blooming
# If there isn’t such day, output -1.

class Solution:
    def kEmptySlots(self, flowers, k):
        #Construct an array to store the days
        days = [0] * len(flowers)
        for day, pos in enumerate(flowers, 1)
            days[pos - 1] = day

        length = len(flowers) - k - 1
        for index in range(length):
            d1 = days[index]
            d2 = days[index + k + 1]
            found = True

            #All days in between must be > d1 & d2
            for day in range(1, k + 1):
                inBetween = days[index + day]
                if inBetween < d1 or inBetween < d2: #Flower has bloomed so break
                    found = False
                    break

            if found:
                return max(d1, d2) #largest of the two

        return -1
