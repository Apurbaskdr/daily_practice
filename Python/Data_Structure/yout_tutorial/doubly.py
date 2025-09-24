class doublyNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last=self.head
            
            return_str= f"[{last.value}]"
            while last.next:
                last=last.next
                return_str += f", {last.value}"
            return_str+="]"
            
            return return_str
            
            
    def __contains__(self, value):
        last=self.head
        while last.next is None:
            if last.value == value:
                return True
            last=last.next
        return False
    
    def __len__(self):
        last=self.head
        count=0
        while last.next is None:
            count+=1
            last=last.next
        return count
            
    
    #appending a value at the end of the linked list
    def append(self, value):
        if self.head is None:
            self.head= doublyNode(value)
            self.tail = self.head
        else:
            last_node = doublyNode(value)
            last_node.prev = self.tail
            self.tail.next=last_node
            self.tail = last_node
            
    
    #adding new head
    def prepend(self, value):
        if self.head is None:
            self.head = doublyNode(value)
            self.tail = self.head
        else:
            first_node=doublyNode(value) #creating a new doublyNode
            first_node.next = self.head
            self.head.prev = first_node
            self.head = first_node
    
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last=self.head
                for i in range(index -1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last=last.next
                    
                new_node=doublyNode(value)
                new_node.next=last.next
                new_node.prev = last
                if last.next is not None:
                    last.next.prev = new_node
                last.next=new_node
                        
                        
    
    def delete(self, value):
        last=self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        if last.next.next is not None:
                            last.next.next.prev = last
                        last.next = last.next.next
                        break
                    last= last.next
    
    def pop(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last=self.head
        for i in range(index-1):
            if last.next is None:
                raise ValueError("Index out of bounds")
            last=last.next
        
        if last.next is None:
            raise ValueError("Index out of bounds")
        else:
            if last.next.next is not None:
                last.next.next.prev = last
            last.next=last.next.next
            
        
            
    
    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last=self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last=last.next
            return last.value
    

    
if __name__ == "__main__":
    ll=DoublyLinkedList()
    
    
    
    ll.append(10) #10
    ll.insert(5, 1) #10,5
    ll.insert(20, 1) #10,20,5
    ll.insert(18, 1) #10,18,20,5
    ll.insert(22, 1) #10,22,18,20,5
    ll.insert(88, 1) #10,88,22,18,20,5
    ll.insert(97, 1) #10,97,88,22,18,20,5
    
    
    
    ll.prepend(100) #100,10,97,88,22,18,20,5
    
    ll.insert(200,1) #100,200,10,97,88,22,18,20,5
    
    ll.delete(18) #100,200,10,97,88,22,20,5
    
    ll.pop(1) #100,10,97,88,22,20,5
    
    
    print(ll)
    
    '''print (ll.get(1))
    
    
    print (29 in ll)
    print (800 in ll)'''