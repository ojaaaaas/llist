#reversing a linked list
class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
    
class linkedList:
    def __init__(self):
        self.head = None

    def reverseLL(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
