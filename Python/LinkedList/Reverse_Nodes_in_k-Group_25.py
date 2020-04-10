#Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or not head.next:return head
        count={}
        index=0
        while head:
            index += 1
            count[index]=head
            head=head.next
        if k>=index: return count[1]
        star=count[k]
        for i in range(1,int(index/k)*k,k):
            for j in range(0,k-1):
                count[i+k-1-j].next=count[i+k-2-j]
            for j in range(0, int(k/2)):
                temp=count[i+j]
                count[i+j]=count[i+k-1-j]
                count[i + k - 1 - j]=temp
        for i in range(k,index,k):
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
head=res.reverseKGroup(head,3)

while head:
    print(head.val)
    head=head.next
