class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

def insertBegining(self,data):
    new_Node = Node(data)
    if self.head is None:
        self.head = new_Node
        return
    else:
        new_Node.next = self.head
        self.head = new_Node

def insertAtIndex(self, data, index):
    if(index == 0):
        self.insertBegining(data)
        return
    
    position = 0
    current_node = self.head

    while(current_node != None and position +1 != index):
        position += 1
        current_node = current_node.next
    
    if current_node != None:
        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node
    else:
        print("Index not found")

def insertEnd(self,data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    current_node = self.head
    while(current_node.next):
        current_node = current_node.next
    current_node.next = new_node
    
def updateNode(self, val, index):
    current_node = self.head
    position = 0
    if position == index:
        current_node.data = val
    else:
        while(current_node != None and position != index):
            position += 1
            current_node = current_node.next
        
        if current_node != None:
            current_node.data = val
        else:
            print("Index not found")

def removeFirstNode(self):
    if self.head is None:
        return
    self.head = self.head.next

def removeLastNode(self):
    if self.head is None:
        return
    curr_node = self.head
    while(curr_node.next != None and curr_node.next.next != None):
        curr_node.next = curr_node
    curr_node.next = None

def removeAtIndex(self, index):
    if self.head is None:
        return
    curr_node = self.head
    position = 0
    if index == 0:
        self.removeFirstNode()
    else:
        while(curr_node != None and position < index -1):
            position += 1
            curr_node = curr_node.next
        
        if curr_node is None and curr_node.next is None:
            print("Index not present")
        else:
            curr_node.next = curr_node.next.next

def printLL(self):
    curr_node = self.head
    while(curr_node):
        print(curr_node.data)
        curr_node = curr_node.next

def sizeOfLL(self):
    size = 0
    if(self.head):
        curr_node = self.head
        while(curr_node):
            size += 1
            curr_node = curr_node.next
        return size
    else:
        return 0
#reverse a LL
def reverseLL(self):
    prev = None
    curr_node = self.head
    while(curr_node):
        next_node = curr_node.next
        curr_node.next = prev
        prev = curr_node
        curr_node = next_node
    self.head = prev
    return self.head

def reverseLLRecursive(self, curr_node, prev):

    if curr_node is None:
        curr_node = self.head

    if curr_node is None:
        self.head = prev
        return  #exit condition
    
    next_node = curr_node.next          #store the next node
    curr_node.next = prev               #reverse the link  
    self.reverseLLRecursive(next_node, curr_node)
