# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        next1 = head
        next2 = head
        while next2 != None and next2.next != None:
            next1 = next1.next
            next2 = next2.next.next
            if next1 == next2:
                return True
        return False
