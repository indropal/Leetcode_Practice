# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        if not head:
            return dummy.next
        # Dummy is set as a temp ListNode which is before the head of Linked List
        # We iterate with the head node & maintain a prev Node which points to the 
        # node before head node.
        # With each iteration, the value of the head node is compared to the value of the 
        # node after the head node -  as long as they are not equal, the prev node & head nodes
        # are updated to next nodes. If they are equal, ONLY the head node is iterated while
        # not updating the prev node until theres a node where head's value is no longer equal to it
        # point the prev.next to this node & continue subsequent iterations till end of list
        prev = dummy

        while head and head.next:

            if head.val != head.next.val:
                prev = prev.next
                head = head.next

            else:
                while head and head.next and head.val == head.next.val:
                    head = head.next

                if (not head) or (not head.next):
                    prev.next = None
                    break

                prev.next = head.next
                head = head.next

                if not head:
                    break

        return dummy.next
