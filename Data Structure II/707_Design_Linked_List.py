class ListNode:
    def __init__(self, value=0):
        self.value = value
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.dummy = ListNode(-999999) # create a dummy node for reference
        self.dummy.next = self.head # this dummy node is used to refer to the head node
        self.tail = self.head # initialize the Tail of the linked list at the head
        self.N = 0

    def get(self, index: int) -> int:
        if self.N <= index:
            return -1
        
        if index == 0:
            # just return head
            return self.head.value

        tmp = self.dummy

        while 0 < index:
            tmp = tmp.next
            index -= 1

        return tmp.next.value

    def addAtHead(self, val: int) -> None:
        tempNode = ListNode(val)

        # Adding a Node for the First time
        if self.N == 0:
            self.head = tempNode
            self.dummy.next = self.head
            self.tail = self.head
            self.N += 1
            return 

        tempNode.next = self.head
        
        # Update the Head Node & Dummy Node pointers
        self.head = tempNode
        self.dummy.next = self.head
        self.N += 1

        # print("Add at Head"); self.printList()

        return

    def addAtTail(self, val: int) -> None:
        
        self.tail.next = ListNode(val)

        # check if this is the first element in the list ~ if so, update head
        if self.N == 0:
            self.head = self.tail.next
            self.dummy.next = self.head

        # update the tail Node pointer
        self.tail = self.tail.next
        self.N += 1

        # print("Add at Tail"); self.printList()

        return

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = ListNode(val)

        if self.N < index:
            # if the index is greater than length of list
            # then it is an invalid index
            return

        if index == 0:
            # then insert before the head of list & update head & dummy pointer
            newNode.next = self.head
            self.head = newNode
            self.dummy.next = self.head

            # if of length 0, then update the tail
            if self.N == 0:
                self.tail = self.head
            
            self.N += 1
            return

        if index == self.N:
            # then insert after the Tail Node
            self.tail.next = newNode
            self.tail = self.tail.next
            self.N += 1
            return

        tmpNode = self.dummy
        # start traversal from before the head node to 
        # arrive at the node before the index
        while tmpNode.next and 0 < index:
            tmpNode = tmpNode.next
            index -= 1
        
        newNode.next = tmpNode.next
        tmpNode.next = newNode
        self.N += 1

        # print("Add at Index"); self.printList()

        return
        
    def deleteAtIndex(self, index: int) -> None:
        
        # flag to tag if tail node no be deleted
        delTail = False if index != self.N-1 else True
        
        if (self.N == 0) or (self.N <= index):
            # there are no Nodes to delete or Index Invalid
            return
        
        if index == 0:
            # Then delete the Head Node
            delNode = self.head
            self.head = self.head.next
            self.dummy.next = self.head

            delNode.next = None
            del delNode
            self.N -= 1

            # print("deleteAtIndex"); self.printList()

            return

        tmpNode = self.dummy

        # traverse to the node before the index-th node
        # update the pointers & delete the node
        while 0 < index:
            tmpNode = tmpNode.next
            index -= 1
        
        delNode = tmpNode.next
        tmpNode.next = delNode.next
        delNode.next = None
        
        del delNode
            
        self.N -= 1
        # print("deleteAtIndex"); self.printList()

        if delTail:
            # update the Tail Node if we've deleted it
            self.tail = tmpNode

        return

    def printList(self) -> None:

        tmpNode = self.head
        print("Number of Nodes:", self.N, end=" | ")
        while tmpNode:
            print(tmpNode.value, end=" -> ")
            tmpNode = tmpNode.next
        
        print("\n")
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)