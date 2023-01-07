# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        # For each iteration, store the object instance address of the List Node in Hash Set
        # for Linked List. While iterating with the second Head check if the List Node is already
        # stored in set if not then there's no intersection

        cache = set()
        lnode = headA
        ans = None

        while lnode:
            cache.add(lnode)
            lnode = lnode.next

        lnode = headB

        while lnode:
            if lnode in cache:
                ans = lnode
                break
            lnode = lnode.next

        return lnode
        """

        # The above solution has Space Complexity of O(N)
        # We might be able to optimizze this further & achieve a soltution with Space Complexity O(1)
        lNodeA, lNodeB = headA, headB

        # BIG IDEA: 
        # We have two pointers to both the Linked List starting at the Head nodes respectively
        # We iterate through each list until arriving at the end of respective list while checking
        # for common nodes in the two lists.
        # If the end of the list is reached, then initialize the Node with the Head node of the other List
        # & iterate through them while checking if they are equal or not
        # This is very similar to checking if a Linked List has a Cycle or not.
        # At a certain point, while the loop continues, there'll be a stage where if there is an intersection
        # the nodes will be equal.
        # if there is no intersection, the loop will eventually terminate when both nodes point to the Tail end
        # i.e. they are None

        while lNodeA != lNodeB:
            lNodeA = headB if not lNodeA else lNodeA.next
            lNodeB = headA if not lNodeB else lNodeB.next

            # Inspect Case when the nodes are equal
            if lNodeA == lNodeB:
                if lNodeA:
                    print(lNodeA, lNodeB, lNodeA.val, lNodeB.val)
                else:
                    print("Both nodes at tail end when they terminate", lNodeA, lNodeB)
                
        return lNodeA