#connect twe increasing linked list make the new list still increasing
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self, pHead1, pHead2):
        if not pHead1:return pHead2
        if not pHead2:return pHead1
        if not pHead1 and pHead2:return
        i, j ,head= pHead1, pHead2,ListNode(0)
        while i and j:
            if i.val<j.val:
                head.next=i
                head=head.next
                i=i.next
            else:
                head.next = j
                head = head.next
                j = j.next
        if not i and j:
            head.next=j
        elif not j and i:
            head.next=i
        if pHead1.val<pHead2.val:return pHead1
        else:return pHead2





l0=ListNode(1)#1
l1=ListNode(5)#2
l2=ListNode(6)#3
l3=ListNode(7)#4
l4=ListNode(8)#5
l5=ListNode(9)#6

l0.next=l1
l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
l5.next=None
head1=l0

L0=ListNode(2)#1
L1=ListNode(3)#2
L2=ListNode(4)#3
L3=ListNode(9)#4
L4=ListNode(10)#5
L5=ListNode(11)#6

L0.next=L1
L1.next=L2
L2.next=L3
L3.next=L4
L4.next=L5
L5.next=None
head2=L0
res=Solution()
root=res.Merge(head1,head2)
while root:
    print(root.val)
    root=root.next












list={'a':2,'b':1,'c':5}
