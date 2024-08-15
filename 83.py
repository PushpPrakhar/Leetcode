# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        currentnode = head

        while currentnode and currentnode.next:
            if currentnode.val == currentnode.next.val:
                currentnode.next = currentnode.next.next
            else:
                currentnode = currentnode.next
        
        return head