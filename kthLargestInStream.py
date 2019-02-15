# Design a class to find the kth largest element in a stream. 
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. 
# For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.
from heapq import heapify, heappush, heappop, heapreplace
class KthLargest:

    def __init__(self, k: 'int', nums: 'List[int]'):
        self.heap = nums
        heapify(self.heap)
        self.k = k
        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: 'int') -> 'int':
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heapreplace(self.heap, val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
