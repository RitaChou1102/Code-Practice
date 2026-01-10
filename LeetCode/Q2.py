# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count1 = ""
        count2 = ""
        count = ""
        while l1:
            count1 = str(l1.val) + count1
            l1 = l1.next
        while l2:
            count2 = str(l2.val) + count2
            l2 = l2.next

        count = str(int(count1) + int(count2))

        ans = ListNode(0)
        current = ans
        
        for i in range(len(count) - 1, -1, -1):
            current.next = ListNode(int(count[i]))
            current = current.next
        return ans.next