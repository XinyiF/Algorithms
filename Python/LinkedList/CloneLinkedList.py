#copy a complex linked list that each node has two pointer, one point to next node, one point to random node
class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

class Solution:
    def Clone(self, pHead):
        if not pHead:return
        count,index,start,random={},0,pHead,{}
        while pHead:
            count[index]=pHead
            index+=1
            pHead=pHead.next
        count[index]=None
        pHead=start
        new_count = {i: j for j, i in count.items()}
        while pHead:
            if pHead.random:
                rand=new_count[pHead.random]
                random[pHead.label]=rand
            else:
                random[pHead.label]=index
            pHead=pHead.next
        head=RandomListNode(start.label)
        start=head
        for i in range(1,index):
            head.next=RandomListNode(count[i].label)
            head=head.next
        head.next=None
        head=start
        while head:
            head.random=count[random[head.label]]
            head=head.next
        return start

















l0=RandomListNode(1)#1
l1=RandomListNode(5)#2
l2=RandomListNode(6)#3
l3=RandomListNode(7)#4
l4=RandomListNode(8)#5
l5=RandomListNode(9)#6

l0.next=l1
l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
l5.next=None
head1=l0

res=Solution()
head=res.Clone(head1)
while head:
    print(head.label)
    head=head.next



