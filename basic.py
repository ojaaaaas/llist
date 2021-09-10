#creating a linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self,prev,new_data):
        if prev is None:
            return

        new_node = Node(new_data)
        new_node.next = prev.next

        prev.next = new_node

    def append_node(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp:
            temp = temp.next

        temp.next = new_node
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__=="__main__":
    llist = linkedList()
    llist.head = Node(2)
    
