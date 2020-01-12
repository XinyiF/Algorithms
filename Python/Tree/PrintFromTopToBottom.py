#Each node of the binary tree is printed from top to bottom,
#and nodes at the same level are printed from left to right
class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res=[]
    def PrintFromTopToBottom(self, root):
        if not root: return []
        stack=[]
        if root.left:
            stack.append(root.left.val)
        if root.right:
            stack.append(root.right.val)
        self.res+=stack
        self.PrintFromTopToBottom(root.left)
        self.PrintFromTopToBottom(root.right)
        return [root.val]+self.res







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

res=[]
result=Solution()
res=result.PrintFromTopToBottom(root)
print(res)