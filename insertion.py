#to insert a node in a linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
#in the front
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

#adding a node after a given node
    def push2(self,new_data,prev):
        new_node = Node(new_data)
        if not prev:
            return None
        
        new_node = Node(new_data)
        new_node.next = prev.next
        prev.next = new_node

    
    def printList(self):
        if Node is None:
            return None
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

#deletion of a complete linked list
    def deleteList(self):
        temp = self.head
        while(temp):
            del temp.data
            temp = temp.next
        print("deleted successfully")
if __name__=="__main__":
    llist = linkedList()
    llist.head = Node(4)
    second = Node(5)
    third = Node(6)

    llist.head.next = second
    second.next = third
    llist.push(8)
    llist.printList()
    print("deleting linked list")
    llist.deleteList()
    