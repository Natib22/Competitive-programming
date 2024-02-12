class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def mynode(self, index):
        current = self.head
        while current and index >= 0:
            current = current.next
            index -= 1
        return current

    def get(self, index: int) -> int:
        if  index >= self.size:
            return -1
        current = self.mynode(index)
        if current:
            return current.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
            
        dummy = self.mynode(index - 1)
        node = Node(val)
        node.next = dummy.next
        dummy.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        dummy = self.mynode(index - 1)
        if dummy.next:
            dummy.next = dummy.next.next
            self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)