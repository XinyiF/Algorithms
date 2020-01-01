#Given a linked list, determine if it has a cycle in it.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        count={}
        if (head == None): return False
        while head:
            if(head not in count):
                count[head]=1
            else:
                return True
            if(head.next!=None):
                head = head.next
            else:
                return False




l0=ListNode(3)
l1=ListNode(2)
l2=ListNode(2)
l3=ListNode(4)

l0.next=l1
l1.next=l2
l2.next=l3
l3.next=None


res=Solution()
r=res.hasCycle(l0)
