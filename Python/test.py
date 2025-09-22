class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def build_linked_list(arr):
        head=None
        tail=None
        for num in arr:
            node=ListNode(num)
            if not head:
                head=node
                tail=node
            else:
                tail.next=node
                tail=node

        return head
    
    

class Solution:
    def rotateRight(self, head: list, k: int):
        print(head,k)



head=[1,2,3,4,5]
k=5
print (head,k)