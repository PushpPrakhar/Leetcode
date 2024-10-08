import math
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        resultList = ListNode()
        ref = resultList

        if l1 is None and l2 is None:
            return resultList.next
        
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val <= l2.val:
            resultList = l1
            l1 = l1.next
        else:
            resultList = l2
            l2 = l2.next
        
        ref= resultList
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                ref.next = l1
                ref = ref.next
                l1= l1.next
            else:
                ref.next = l2
                ref = ref.next
                l2 = l2.next
        
        if l1 is None:
            ref.next = l2
        else:
            ref.next = l1
        
        return resultList