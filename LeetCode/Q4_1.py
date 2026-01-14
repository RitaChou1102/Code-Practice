class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # O((m+n)log(m+n))
        m = len(nums1)
        n = len(nums2)
        num = sorted(nums1 + nums2)
        l = m + n
        if l % 2 == 0:
            ans = (num[(l//2) - 1] + num[l//2]) / 2.0
        else:
            ans = num[(l//2)]
        return ans