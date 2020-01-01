#delete current node
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next



l0=ListNode(3)
l1=ListNode(2)
l2=ListNode(5)
l3=ListNode(4)
l4=ListNode(8)
l5=ListNode(9)

l0.next=l1
l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
l5.next=None
head=l0
node=head.next #l1
res=Solution()
res.deleteNode(node)
while head:
    print(head.val)
    head=head.next