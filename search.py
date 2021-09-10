#searching an element in a linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.next = None
    
    #iterative search
    def searchEle(self,ele):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            if(ele == temp.data):
                return True
            else:
                
                temp = temp.next
        return False
    
    #recursive search
    def searchRec(self,li,ele):
        if not li:
            return False
        if(li.data == ele):
            return True
        return self.searchRec(li.next,ele)
        
    
    #print middle of a LL
    def printMiddle(self):
#two pointers slow takes one step and fast takes two.By the time fast reaches the end slow reaches middle
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            print("The middle element is", slow.data)

    #get nth node
    def getNth(self,idx):
        
        temp = self.head
        count = 0
        while temp:
            if count == idx:
                return temp.data
            count +=1
            temp = temp.next
        assert(False)
        return 0

    #int count
    def intCount(self,key):
        temp = self.head
        count = 0
        while temp:
            if temp.data == key:
                count += 1
            temp = temp.next
        return count
        





if __name__=="__main__":
    llist = linkedList()
    llist.head = Node(3)
    llist.head.next = Node(4)
    llist.head.next.next = Node(5)
    print(llist.searchEle(6))
    llist.printMiddle()
    print(llist.searchRec(llist.head,4))
    print(llist.getNth(llist.head,2))
        