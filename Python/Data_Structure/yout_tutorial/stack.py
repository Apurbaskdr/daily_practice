class stackNode:
    def __init__(self, head):
        self.head = head
        self.next = None
        
class stack:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        if self.head == None:
            first_node=stackNode(value)
            self.head = first_node
        else:
            first_node = stackNode(value)
            first_node.next=self.head
            self.head=first_node
            
    def pop(self):
        if self.head == None:
            raise ValueError("List is empty!!")
        else:
            node_to_remove=self.head
            if self.head.next == None:
                self.head=None
            else:
                
        