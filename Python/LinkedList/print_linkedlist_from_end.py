class Solution:
    def printListFromTailToHead(self, listNode):
        array=[]
        while listNode:
            array.append(listNode.val)
            listNode=listNode.next
        return array[::-1]


