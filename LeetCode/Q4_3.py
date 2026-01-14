class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # O(m+n)
        m = len(nums1)
        n = len(nums2)
        l = m + n

        p1 = 0 
        p2 = 0
        
        flag = 0
        mid = 0
        count = 0
        ans = 0.0

        if l % 2 == 0:
            flag = 0
            mid = (l//2) - 1
        else:
            flag = 1
            mid = (l//2)

        while p1 < m and p2 < n:
            if count == mid:
                if flag == 0:
                    if nums1[p1] <= nums2[p2]:
                        try:
                            ans = (nums1[p1] + min(nums1[p1 + 1], nums2[p2])) / 2.0
                        except:
                            ans = (nums1[p1] + nums2[p2]) / 2.0
                    else:
                        try:
                            ans = (nums2[p2] + min(nums2[p2 + 1], nums1[p1])) / 2.0
                        except:
                            ans = (nums2[p2] + nums1[p1]) / 2.0
                else:
                    ans = min(nums1[p1], nums2[p2])
                break

            if nums1[p1] <= nums2[p2]:
                p1 += 1
            else:
                p2 += 1
            count += 1
        else:
            if p1 < m:
                for i in range(len(nums1)):
                    if count == mid:
                        if flag == 0:
                            ans = (nums1[p1] + nums1[p1 + 1]) / 2.0
                        else:
                            ans = nums1[p1]
                        break
                    p1 += 1
                    count += 1
            elif nums2:
                for i in range(len(nums2)):
                    if count == mid:
                        if flag == 0:
                            ans = (nums2[p2] + nums2[p2 + 1]) / 2.0
                        else:
                            ans = nums2[p2]
                        break
                    p2 += 1
                    count += 1
        
        return ans