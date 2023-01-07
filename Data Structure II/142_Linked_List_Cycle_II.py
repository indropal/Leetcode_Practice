# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        if (not head) or (not head.next):
            return

        address = {} # Use Hash Map to store the Address of the ListNode
        tmpNode, ans = head, None

        while tmpNode:
            if tmpNode not in address:
                address[tmpNode] = 1
            else:
                ans = tmpNode
                break
            tmpNode = tmpNode.next

        return ans
        """

        # The above solution has space complexity O(N)
        # We can optimize this further by using the "Hare & Tortorise algorithm"
        # to achieve a solution utilizing O(1) memory
        
        if (not head) or (not head.next):
            return

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        
        if (not fast.next) or (not fast.next.next):
            # make sure the loop did not terminate because of end of list
            # there could be a chance that fast.next.next is None & terminates 
            # Hare - Rabbit traversals
            return

        # iterate to the beginning of the list so that we arrive at the beginning of the cycle
        while slow and (head != slow):
            slow = slow.next
            head = head.next

        return head