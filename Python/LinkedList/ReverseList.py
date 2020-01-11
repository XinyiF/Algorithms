#reverse a linked list
class Solution:
    def ReverseList(self, pHead):
        if pHead==None:return None
        count,index={},0
        while pHead:
            index+=1
            count[index]=pHead
            pHead= pHead.next
        head=count[index]
        start=head
        for i in range(index-1,0,-1):
            head.next=count[i]
            head=count[i]
        head.next=None
        return start




