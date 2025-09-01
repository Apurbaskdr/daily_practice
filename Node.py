class Node:
    def __init__(self,value,next_node=None):
        self.value=value
        self.next_node=next_node
    
    def set_next_node(self,next_node):
        self.next_node=next_node
    
    def get_next_node(self):
        return self.next_node
    
    def get_value(self):
        return self.value
    
    
        




a=Node(9)
b=Node(10)
res1=Node.get_value(a)
res2=Node.get_value(b)
res3=Node.set_next_node(a,b)
print(res1,res2,res3)