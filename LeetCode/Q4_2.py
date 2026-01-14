class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # O((m+n)^2)
        m = len(nums1)
        n = len(nums2)
        l = m + n
        num = []
        flag = 0
        mid = 0
        count = 0
        ans = 0

        if l % 2 == 0:
            flag = 0
            mid = (l//2) - 1
        else:
            flag = 1
            mid = (l//2)

        while nums1 and nums2:
            if count == mid:
                if flag == 0:
                    if nums1[0] <= nums2[0]:
                        try:
                            ans = (nums1[0] + min(nums1[1], nums2[0])) / 2.0
                        except:
                            ans = (nums1[0] + nums2[0]) / 2.0
                    else:
                        try:
                            ans = (nums2[0] + min(nums2[1], nums1[0])) / 2.0
                        except:
                            ans = (nums2[0] + nums1[0]) / 2.0
                else:
                    ans = min(nums1[0], nums2[0])

                break

            if nums1[0] <= nums2[0]:
                del nums1[0]
            else:
                del nums2[0]

            count += 1
        else:
            if nums1:
                for i in range(len(nums1)):
                    if count == mid:
                        if flag == 0:
                            ans = (nums1[0] + nums1[1]) / 2.0
                        else:
                            ans = nums1[0]
                        break

                    del nums1[0]
                    count += 1
            elif nums2:
                for i in range(len(nums2)):
                    if count == mid:
                        if flag == 0:
                            ans = (nums2[0] + nums2[1]) / 2.0
                        else:
                            ans = nums2[0]
                        break

                    del nums2[0]
                    count += 1

        return ans