# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 

        # Algorithm:
        # The idea is to divide the list into two parts from the midddle
        # The second half of the list is taken and while iterating through each node
        # we break it off from the second-half of list one ata time & store it into a stack
        # ~ eventually, the last element in the entire list / second-half of the list
        # ends up at the top of the stack.
        # Then iterate through the first half of the list - at each iteration step, 
        # pop an element from the stack & insert it after the node which is currently pointed to 
        # while traversal.
        # Corener case being the last node pointing to itself in case of list with enven number of
        # nodes in entire list.

        stack = []
        N = 0
        tmpNode = head

        while tmpNode:
            N += 1
            tmpNode = tmpNode.next
        
        if N < 3:
            # the order of the list never changes
            return
        
        # get the length of the list & get mid-length
        numIter = N // 2
        tmpNode = head

        # iterate to the middle of the list
        while numIter:
            tmpNode = tmpNode.next
            numIter -= 1
        
        numIter = N // 2
        
        # pointing to middle of the list - break the list into 2 halves
        # while iterating through the second half, break off each node
        # and include it into a stack (each node independently)
        while tmpNode:
            node = tmpNode
            tmpNode = tmpNode.next
            node.next = None
            stack.append(node)

        tmpNode = head

        while stack:
            # iterate throgh first half of the list while popping from stack 
            # & inserting the popped node into the list
            node = stack.pop()
            tmpNodeNext = tmpNode.next
            tmpNode.next = node
            node.next = tmpNodeNext

            tmpNode = tmpNodeNext
        
        if N%2 == 0:
            # For even number of Nodes in list, the last node will cause a self-loop / cycle reference
            # where the next pointer points to itself. Therefore, to avoid this, set this last node next
            # reference to None
            tmpNode.next = None

        return
