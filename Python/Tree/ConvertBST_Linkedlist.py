#convert a BST to a double Linked list
class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:return
        address,value,stack,cur,index,sor={},{},[],pRootOfTree,0,[]
        while stack or cur:
            while cur:
                stack.append(cur)
                address[index]=cur
                value[index]=cur.val
                index+=1
                sor.append(cur.val)
                cur=cur.left
            top= stack.pop()
            cur=top.right
        sor=sorted(sor)
        sor_index=[]
        new_value= {i: j for j, i in value.items()}
        for i in sor:
            sor_index.append(new_value[i])
        for i in range(len(sor_index)-1):
            address[sor_index[i]].right=address[sor_index[i+1]]
            address[sor_index[i+1]].left=address[sor_index[i]]
        return address[sor_index[0]]








#          7
#        /   \
#       5     10
#      / \   / \
#     2   6 8   11
tree=TreeNode(7)
tree.left=TreeNode(5)
tree.right=TreeNode(10)
tree.left.left=TreeNode(2)
tree.left.right=TreeNode(6)
tree.right.left=TreeNode(8)
tree.right.right=TreeNode(11)


s=Solution()
s.Convert(tree)

