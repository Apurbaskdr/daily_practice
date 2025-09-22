class node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    
    #going to traverse the list and print the value
    def __repr__(self):
        pass

    def __contains__(self, value):
        last=self.head
        while last is not None:
            if last.value == value:
                return True
            last=last.next
        return False


    def __len__(self):
        pass

    def append(self,value):
        if self.head is None:
            self.head = node(value)
        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=node(value)
    #Placing a value at the 1st position
    def prepend(self,value):
        #Creating a node with the value
        first_node=node(value)
        #Poining to the current head node
        first_node.next=self.head
        #assigning the new node as head
        self.head=first_node

    def insert(self, value, index):
        #if we are inserting new value at the 1st position
        if index == 0:
            self.prepend(value)
        #if there is not such list available
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last=self.head
                
                #will traverse till the index element
                for i in range(index-1):
                    if last.next == None:
                        raise ValueError("Index out of bounds")
                    #if the for loop will process successfully then last will keep the index-1 node's point
                    last=last.next
                #creating new node
                new_node = node(value)
                #new node is pointing to the index node
                new_node.next=last.next
                #index-1 node is pointing to the new_node
                last.next=new_node
                          

    def delete(self, value):
        pass

    def pop(self,index):
        pass

    def get(self,index):
        pass

    def print(self):
        pass

if __name__== "__main__":
    pass
        