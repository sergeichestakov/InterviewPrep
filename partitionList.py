# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
class Solution:
    def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':
        lessThan, greaterThan = None, None
        ltPtr, gtPtr = None, None
        curr = head
        while curr: # Populate less than and greater than lists
            if curr.val < x:
                if not lessThan:
                    lessThan = ListNode(curr.val)
                    ltPtr = lessThan
                else:
                    lessThan.next = ListNode(curr.val)
                    lessThan = lessThan.next
            else:
                if not greaterThan:
                    greaterThan = ListNode(curr.val)
                    gtPtr = greaterThan
                else:
                    greaterThan.next = ListNode(curr.val)
                    greaterThan = greaterThan.next
            
            curr = curr.next
         
        ret = ltPtr # Return list starts with less list
        curr = ret
        
        if curr: # Get to the end of the list
            while curr.next:
                curr = curr.next
        else: # Less than list is empty
            ret = gtPtr
            curr = ret
            if not gtPtr:
                return ret
            gtPtr = gtPtr.next
            
        while gtPtr: # Get to the end of the greaterthan list
            curr.next = gtPtr
            gtPtr = gtPtr.next
            curr = curr.next
            
        return ret
