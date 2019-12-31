#Given a linked list, return the node where the cycle begins. If there is no cycle, return null.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        count={}
        if (head == None): return None
        index=0
        while head:
            if(head not in count):
                count[head]=index
            else:
                return head
            if(head.next!=None):
                head = head.next
            else:
                return None
            index+=1




l0=ListNode(3)
l1=ListNode(2)
l2=ListNode(2)
l3=ListNode(4)

l0.next=l1
l1.next=l2
l2.next=l3
l3.next=l2


res=Solution()
r=res.hasCycle(l0)
print(r)
