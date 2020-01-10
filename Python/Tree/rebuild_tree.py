#rebuild a BST based on preorder and inorder traversal
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if len(pre)==0 or len(tin)==0:return None
        head=TreeNode(pre[0])
        mid = tin.index(pre[0])
        head.left = self.reConstructBinaryTree(pre[1:mid + 1], tin[:mid])
        head.right = self.reConstructBinaryTree(pre[mid + 1:], tin[mid + 1:])
        return head


















    def preorder_print(self,start,res):
        if start:
            res.append(start.val)
            res=self.preorder_print(start.left,res)
            res= self.preorder_print(start.right, res)
        return res
#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)


resu=[]
pre=[1,2,4,5,6,3,7]
tin=[4,2,5,1,6,3,7]
res=Solution()
tree=res.reConstructBinaryTree(pre,tin)
print(res.preorder_print(tree,resu))