# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            # There are no nodes in the Linked List
            return head

        # Create Dummy reference pointer
        dummy = ListNode()
        dummy.next = head

        swapNode1 = head
        swapNode2 = head.next
        headFlag = True # flag for keeping track if head is involved in Swapping

        if not swapNode2:
            # There is only one node in the Linked List
            return head
        
        while swapNode2:
            # start swapping the nodes
            swapNode1.next = swapNode2.next
            dummy.next = swapNode2
            swapNode2.next = swapNode1

            if headFlag:
                head = swapNode2
                headFlag = False

            # update to move to the next Pair
            dummy = swapNode1
            swapNode1 = swapNode1.next

            if not swapNode1:
                # No nodes left to swap
                break
            
            swapNode2 = swapNode1.next

        return head