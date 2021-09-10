#finding the length of a linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def lenList(self):
        length = 0
        temp = self.head
        while(temp):
            length += 1
            temp = temp.next
        print(length) 
    
if __name__=="__main__":
    llist = linkedList()
    llist.head = Node(2)
    llist.head.next = Node(3)
    llist.head.next.next = Node(4)
    llist.lenList()

        