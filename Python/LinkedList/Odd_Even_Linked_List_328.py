#Given a singly linked list, group all odd nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next: return head
        odd,oddhead=head,head
        even,evenhead=head.next,head.next
        head=head.next.next
        while head:
            oddhead.next=head
            oddhead=head
            evenhead.next=head.next
            evenhead=head.next
            if head.next and head.next.next:
                head=head.next.next
            else:break
        head.next=even
        return odd



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
res=Solution()
head=res.oddEvenList(head)

while head:
    print(head.val)
    head=head.next