def rotate(ls,num):
    i=0
    while i<num:
        last_value=ls.pop(-1)
        list_with_last_value=[]
        list_with_last_value.append(last_value)
        ls=list_with_last_value+ls
        i=i+1
    return ls


#print(rotate([1,2,3,4,5],2)) #[4,5,1,2,3]

print(rotate([0,1,2],4)) #[2,0,1]


'''i=0
        while i<k: 
            second_last=head
            while second_last.next.next:
                second_last=second_last.next

            last=second_last.next
            second_last.next=None
            last.next=head
            head=last
            i+=1
        return head
        '''


'''class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Effective rotations
        k = k % length
        if k == 0:
            return head

        # Step 3: Connect tail to head (make it circular)
        tail.next = head

        # Step 4: Find new head (length - k steps from start)
        steps_to_new_head = length - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None  # break the circle

        return new_head'''