class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.head = Node()

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        pos = self.head
        i = 0
        while i <= index and pos is not None:
            pos = pos.next
            i+=1
        if pos:
            return pos.val
        else:
            return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val=val)
        new_node.next=self.head.next
        self.head.next = new_node

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val=val)
        pos = self.head
        while pos.next is not None:
            pos = pos.next
        pos.next = new_node

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        new_node = Node(val=val)
        pos = self.head
        i = 0
        while i < index and pos.next is not None:
            pos = pos.next
            i+=1
        if i == index:
            new_node.next = pos.next
            pos.next = new_node

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        pos = self.head
        i = 0
        while i < index and pos.next is not None:
            pos = pos.next
            i+=1
        if pos.next:
            pos.next = pos.next.next

if __name__ == '__main__':
    # Your MyLinkedList object will be instantiated and called as such:
    obj = MyLinkedList()
    print(obj.addAtHead(7))
    print(obj.addAtHead(2))
    print(obj.addAtHead(1))
    print(obj.addAtIndex(3, 0))
    print(obj.deleteAtIndex(2))
    print(obj.addAtHead(6))
    print(obj.addAtTail(4))
    print(obj.get(4))
    print(obj.addAtHead(4))
    print(obj.addAtIndex(5, 0))
    print(obj.addAtHead(6))

