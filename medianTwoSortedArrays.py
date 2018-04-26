# Find the median of 2 sorted arrays
class Solution:
    def median(self, arr):
        if len(arr) == 0:
            return None
        length = len(arr)
        mid = length // 2
        if length % 2 == 0:
            return (arr[mid] + arr[mid - 1]) / 2.0
        else:
            return arr[mid]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0:
            return self.median(nums2)
        elif len(nums2) == 0:
            return self.median(nums1)

        #Both non empty
        combLen = len(nums1) + len(nums2)
        medIndex = combLen // 2
        i1 = 0
        i2 = 0
        prev = nums1[0]
        curr = nums2[0]
        while medIndex > 0:
            if(nums1[i1] < nums2[i2]):
                if i1 < len(nums1) - 1:
                    prev = curr #save the previous value
                    i1 += 1
                    curr = nums1[i1] if nums1[i1] < nums2[i2] else nums2[i2] #smaller of the two
                elif i2 < len(nums2) - 1: #reached the end of array 1, keep track of array 2
                    prev = curr
                    curr = nums2[i2]
                    i2 += 1
            else:
                if i2 < len(nums2) - 1:
                    prev = curr
                    i2 += 1
                    curr = nums1[i1] if nums1[i1] < nums2[i2] else nums2[i2] #smaller of the two
                elif i1 < len(nums1) - 1: #end of array 2, keep track of array 1
                    prev = curr
                    curr = nums1[i1]
                    i1 += 1

            medIndex -= 1
        if combLen % 2 == 0: #Even
            return (curr + prev) / 2.0
        else:
            return curr
