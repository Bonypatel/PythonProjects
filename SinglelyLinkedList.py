class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next # can't be self.head because the dummy node is the head
        i = 0

        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next # Have to do this first because the dummy node exists
        self.head.next = new_node

        if not new_node.next: # only if the list was empty before inserting
            self.tail = new_node 

    def insertTail(self, val: int) -> None:
        # if the list is empty then tail points at the dummy node
        # also works if the list is not empty.
        self.tail.next = ListNode(val)
        self.tail = self.tail.next


    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            #Move curr to node before target node while taking care for the index not existing
            i += 1
            curr = curr.next

        if curr and curr.next: # Target node and the node before exists
            if curr.next == self.tail:
                self.tail = curr # handle the end of the linked list edge case
            curr.next = curr.next.next
            return True
        return False
        

    def getValues(self) -> list[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

        
