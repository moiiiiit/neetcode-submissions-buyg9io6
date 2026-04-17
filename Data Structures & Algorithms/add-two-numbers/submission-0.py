# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = None
        ptr3 = None
        ptr1 = l1
        ptr2 = l2
        carry = 0
        while ptr1 or ptr2:
            operand1 = 0
            operand2 = 0
            if ptr1:
                operand1 = ptr1.val
            if ptr2:
                operand2 = ptr2.val

            val = (operand1 + operand2 + carry) % 10
            carry = math.floor((operand1 + operand2 + carry) / 10)
            if ptr3:
                ptr3.next = ListNode(val, None)
                ptr3 = ptr3.next
            else:
                l3 = ListNode(val, None)
                ptr3 = l3

            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None

        if carry:
            ptr3.next = ListNode(carry, None)

        return l3
