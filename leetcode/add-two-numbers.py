# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ans = ListNode()
        current = ans

        while l1 or l2:
            s = current.val

            if l1:
                s += l1.val
                l1 = l1.next

            if l2:
                s += l2.val
                l2 = l2.next
            
            current.val = s % 10
            carry = s // 10

            if l1 or l2 or carry:
                current.next = ListNode(carry)

            current = current.next

        return ans