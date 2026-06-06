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





"""
0 --> 1 --> 2 --> 3 
head is 0
current is 0
nxt is 1
we want for 0 to have None for next
we want 1 to have 0 for next
node0 
val = 0
next = node1
"""
        