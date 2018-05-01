# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# Total complexity is O(n + n + nlog(n)) = O(nlog(n)) as creating the array and converting it to a heap both run in linear time
# While removing the smallest item in a heap is an O(log(n)) operation and must be done for all n nodes

from heapq import heapify, heappop

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for head in lists: #Insert every value into an array O(n)
            while head:
                heap.append(head.val)
                head = head.next

        if len(heap) == 0: #Empty list
            return

        heapq.heapify(heap) #Create a heap O(n)
        first = heapq.heappop(heap)
        head = ListNode(first) #Maintain one pointer to the head and another to the end of the list
        curr = head

        while heap: #Pop every item off of the heap in order until it's empty O(nlog(n))
            smallest = heapq.heappop(heap)
            curr.next = ListNode(smallest)
            curr = curr.next

        return head

