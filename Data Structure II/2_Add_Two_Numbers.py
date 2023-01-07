# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total, carry = 0, 0
        dummy1, dummy2 = l1, l2
        
        while dummy1 and dummy2:
            total = dummy1.val + dummy2.val + carry
            carry = total // 10
            total = total%10

            dummy1.val = total

            dummy1 = dummy1.next
            dummy2 = dummy2.next

        if dummy1:
            # if there are more nodes in dummy1 than dummy2 ~ continue
            while dummy1:
                total = dummy1.val + carry
                carry = total // 10
                total = total%10
                
                dummy1.val = total
                dummy1 = dummy1.next
        else:
            # there are more nodes in dummy2 rather than dummy1
            # traverse till the end of list to update till tail of list
            dummy1 = l1
            while dummy1.next:
                dummy1 = dummy1.next

            while dummy2:
                total = dummy2.val + carry
                carry = total // 10
                total = total%10

                dummy1.next = ListNode(total)
                dummy1 = dummy1.next
                dummy2 = dummy2.next

        # check for any trailing Carries
        if 0 < carry:
            # traverse till the end of list
            dummy1 = l1
            while dummy1.next:
                dummy1 = dummy1.next

            dummy1.next = ListNode(val= carry)
            dummy1 = dummy1.next

        return l1