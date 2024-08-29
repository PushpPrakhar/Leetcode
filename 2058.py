# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minDistance = math.inf
        firstIndex = -1
        prevIndex = -1
        index = 1
        prev = head
        curr = head.next

        while curr.next:
            if curr.val > prev.val and curr.val > curr.next.val or \
         curr.val < prev.val and curr.val < curr.next.val:
                if firstIndex == -1:
                    firstIndex = index
                if prevIndex != -1:
                    minDistance = min(minDistance, index - prevIndex)
                prevIndex = index
            prev = curr
            curr = curr.next
            index += 1
        
        if minDistance == math.inf:
            return [-1,-1]
        return [minDistance, prevIndex - firstIndex]