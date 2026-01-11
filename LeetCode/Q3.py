class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Sliding Window

        l = len(s)
        s1 = set()
        length = 0
        left = 0
        for right in range(l):
            while s[right] in s1:          
                s1.remove(s[left])
                left += 1
            s1.add(s[right])
            if len(s1) > length:
                length = len(s1)
        return length