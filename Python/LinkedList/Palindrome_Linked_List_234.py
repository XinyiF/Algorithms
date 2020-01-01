#Given a singly linked list, determine if it is a palindrome.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        if head==None and head.next==None:
            return True
        elif head.next.next==None:
            if head.val==head.next.val:return True
            else:return False
        fast,slow=head,head
        count={}
        index=0
        while fast:
            count[slow.val]=index
            fast=fast.next.next
            slow= slow.next
            index+=1
            if not fast:
                head= slow
                break
            elif not fast.next:
                head=slow.next
                break
        index-=1
        while head:
            if not head.val in count or count[head.val]!=index:
                return False
            else:
                index-=1
                head=head.next
        return True


l0=ListNode(1)
l1=ListNode(0)
l2=ListNode(0)
#l3=ListNode(2)
#l4=ListNode(3)

l0.next=l1
l1.next=l2
l2.next=None
#l3.next=l4
#l4.next=None
head=l0
res=Solution()
print(res.isPalindrome(head))

