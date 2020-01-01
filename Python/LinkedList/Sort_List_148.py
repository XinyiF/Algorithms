#sort a list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def cover(self, a):
        b = []
        while a:
            b.append(a.val)
            a = a.next
        return b
    def sortList(self, head):
        if not head:
            return head
        r = self.cover(head)
        r.sort()
        first = r.pop(0)
        temp = ListNode(first)
        node = temp
        for j in r:
            node.next = ListNode(j)
            node = node.next
        return temp


l0 = ListNode(3)
l1 = ListNode(-2)
l2 = ListNode(2)
l3 = ListNode(1)

l0.next = l1
l1.next = l2
l2.next = l3
l3.next = None
head = l0

res=Solution()
res.sortList(head)
print('Hi')
while head:
    print(head.val)
    head=head.next
