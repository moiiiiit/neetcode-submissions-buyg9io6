# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        self.helper(head)
        head.next=None
        return self.tail
    
    def helper(self, ptr):
        if not ptr.next:
            self.tail = ptr
            return ptr
        next_ptr = self.helper(ptr.next)
        if next_ptr:
            next_ptr.next = ptr
        return ptr
