# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k==1:
            return head

        N = 0
        # create dummy reference pointer for head node
        dummy = ListNode()
        dummy.next = head

        tmpNode = head

        while tmpNode:
            N += 1
            tmpNode = tmpNode.next

        def reverseList(start, end):
            # Function to reverse the linked list
            stack = []
            node = start
            while node:
                tmpNode = node
                node = node.next
                tmpNode.next = None
                stack.append(tmpNode)

            firstFlag = True
            dummyK = ListNode()
            while stack:
                node = stack.pop()
                if firstFlag:
                    start = node
                    firstFlag = False

                dummyK.next = node
                dummyK = dummyK.next
            
            if k%2 == 0:
                # for even length of list ensure there are no self-loops
                dummyK.next = None
            end = dummyK
            
            return (start, end)

        numTraverse = N//k
        # Keep track of the nodes ~'preTnp' is pointer to keep track of node before start of k-length list
        tmpNode, preTmp = head, dummy
        headFlag = True # indicating if the head pointer needs to be updated
        startNode, endNode = None, None
        
        while numTraverse:
            startNode = tmpNode
            # iterate to end of k-length i.e. we want to end iteration while pointing to kth node
            iterCnt = k
            while tmpNode.next and 1 < iterCnt:
                tmpNode = tmpNode.next
                iterCnt -= 1
            
            # set the end-node as the kth node in list
            endNode = tmpNode
            tmpNode = tmpNode.next # iterate to the remaining part of the list
            endNode.next = None # break the list of k-length from original list
            
            # we need to reverse the list from start-node till end-node [both nodes included]
            # print(startNode.val, endNode.val)
            (startNode, endNode) = reverseList(startNode, endNode); #print(startNode.val, endNode.val)
            endNode.next = tmpNode # join with rest of the list by linking reversed k-length list 
            
            # join with original list by linking reversed k-length list with node prev. to start node
            preTmp.next = startNode
            # update the pointer for node prev. to start node as end-node of k-length list
            # for it to serve as prev. node for start node of next k-length list
            preTmp = endNode 

            if headFlag:
                # if it is the first k-length list in original list then update the head pointer
                head = startNode
                dummy.next = head
                headFlag = False

            numTraverse -= 1

        return head
        
