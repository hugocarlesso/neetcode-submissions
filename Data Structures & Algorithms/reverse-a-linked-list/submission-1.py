# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        previous = None
        while current is not None:
            nxt = current.next # temp for next
            current.next = previous # shift link
            previous = current # shift prev
            current = nxt # shift current
        return previous
        