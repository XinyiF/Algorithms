#find the path from root to leaf whose sum is a expected number
class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath_recursive(self, root, expectNumber):
        if not root:
            return []
        if root and expectNumber==root.val and not root.left and not root.right:
            return [[root.val]]
        res=[]
        left=self.FindPath(root.left, expectNumber-root.val)
        right=self.FindPath(root.right, expectNumber-root.val)
        for i in left+right:
            res.append([root.val]+i)
        return res

    def FindPath(self,root,expectNumber):
        if not root:
            return []
        stack,cur,temp,path,res=[root],root,root.val,[root.val],[]
        while stack:
            if cur and cur.val<expectNumber-temp:
                cur=cur.left
                temp+=cur.val
                path.append(cur.val)
            elif cur and cur.val>expectNumber-temp:
                cur=stack.pop().right
                path.pop()
                pass







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
print(s.FindPath(tree,18))
