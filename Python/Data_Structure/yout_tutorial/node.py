class node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
    
class LinkedList:
    def __init__(self):
        self.head = None
    
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
            self.head= node(value)
        else:
            last= self.head
            while last.next:
                last=last.next
            last.next=node(value)
    
    #adding new head
    def prepend(self, value):
        first_node=node(value) #creating a new node
        first_node.next = self.head
        self.head=first_node
    
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
                    
                new_node=node(value)
                new_node.next=last.next
                last.next=new_node
                        
                        
    
    def delete(self, value):
        last=self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
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
    ll=LinkedList()
    
    ll.append(10)
    ll.append(5)
    ll.append(18)
    ll.append(22)
    ll.append(29)
    
    
    
    ll.prepend(100)
    ll.insert(200,1)
    ll.delete(18)
    print(ll.pop(1))
    
    
    print(ll)
    
    print (ll.get(1))
    
    
    print (29 in ll)
    print (800 in ll)