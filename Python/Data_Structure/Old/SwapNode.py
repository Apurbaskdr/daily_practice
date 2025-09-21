import Node
from linkedlist import linked_list

class SwapNode:
    def swap_node(input_list,val1,val2):
        node1_prev=None
        node2_prev=None
        node1=input_list.head_node
        node2=input_list.head_node

        if val1==val2:
            print ("Both values are same, no need of swapping")
            return
        
        while node1 is not None:
            if node1.get_value() == val1:
                break
            node1_prev=node1
            node1=node1.get_next_node()
        
        while node2 is not None:
            if node2.get_value() == val2:
                break
            node2_prev=node2
            node2=node2.get_net_value()
        
        if node1 is None or node2 is None:
            print ("Swap is not possible as one or two values are not present in the list")
            return
        
        if node1_prev is None:
            input_list.head_node = node2
        else:
            node1_prev.set_next_value(node2)
        
        if node2_prev is None:
            input_list.head_node = node1
        else:
            node2_prev.set_next_value(node1)



        temp=node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)


l1=linkedlist.linked_list()
for i in range(10):
    l1.insert_beginning(i)

print (l1.stringify_list())
SwapNode(11,9,5)
print (l1.stringify_list())