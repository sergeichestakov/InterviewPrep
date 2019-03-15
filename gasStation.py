# There are N gas stations along a circular route, 
# where the amount of gas at station i is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to 
# travel from station i to its next station (i+1). 
# You begin the journey with an empty tank at one of the gas stations.
# Return the starting gas station's index if you can travel around the circuit 
# once in the clockwise direction, otherwise return -1.
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: 
        tank = res = total = 0
        
        for index in range(len(gas)):
            tank += gas[index] - cost[index]
            if tank < 0:
                total += tank
                tank = 0
                res = index + 1
                
        total += tank
        return res if total >= 0 else -1
