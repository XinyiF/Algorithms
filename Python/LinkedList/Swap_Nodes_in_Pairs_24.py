#Given a linked list, swap every two adjacent nodes and return its head.

#You may not modify the values in the list's nodes, only nodes itself may be changed.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:return head
        star=head.next
        count={}
        index=0
        while head:
            index += 1
            count[index]=head
            head=head.next
        for i in range(1,index,2):
            count[i+1].next=count[i]
            temp=count[i+1]
            count[i+1]=count[i]
            count[i]=temp
        for i in range(2,index,2):
            count[i].next=count[i+1]
        count[index].next=None
        return star






l0=ListNode(3)#1
l1=ListNode(2)#2
l2=ListNode(5)#3
l3=ListNode(4)#4
l4=ListNode(8)#5
l5=ListNode(9)#6

l0.next=l1
l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
l5.next=None
head=l0
res=Solution()
head=res.swapPairs(head)

while head:
    print(head.val)
    head=head.next
