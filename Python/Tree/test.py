class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root=TreeNode(root)

    def print_tree(self,traversal_type):
        if traversal_type=="preorder":
            return self.preorder_print(tree.root,"")
        else:print("maybe later")


    def preorder_print(self,start,res):
        if start:
            res.append(start.val)
            res=self.preorder_print(start.left,res)
            res= self.preorder_print(start.right, res)
        return res

    def inorder_print(self,start,res):
        if start:
            res = self.inorder_print(start.left, res)
            res.append(start.val)
            res = self.inorder_print(start.right, res)
        return res

    #def postorder_print(self,start,res):
     #   if start:
      #      res = self.inorder_print(start.left, res)
      #      res = self.inorder_print(start.right, res)
       #     res.append(start.val)
       # return res


    def inorderTraversal_recursive(self, root):
        res=[]
        def print_tree(root):
            if not root:
                return
            print_tree(root.left)
            res.append(root.val)
            print_tree(root.right)
        print_tree(root)
        return res

    def preorderTraversal(self, root):
            res = []  # store result
            stack = []  # helper stack
            cur = root  # current node
            while stack or cur:
                while cur:
                    res.append(cur.val)
                    stack.append(cur)
                    cur = cur.left
                top = stack.pop()
                cur = top.right
            return res

    def inorderTraversal(self, root):
        res=[]
        stack=[]
        cur=root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur=cur.left
            top=stack.pop()
            res.append(top.val)
            cur=top.right
        return res

    def postorderTraversal(self, root):
            res = []
            stack = []
            cur = root
            while stack or cur:
                while cur:
                    res.append(cur.val)
                    stack.append(cur)
                    cur = cur.right
                top = stack.pop()
                cur = top.left
            return res[::-1]




#          7
#        /   \
#       5     10
#      / \   / \
#     2   6 8   11
tree=BinaryTree(7)
tree.root.left=TreeNode(5)
tree.root.right=TreeNode(10)
tree.root.left.left=TreeNode(2)
tree.root.left.right=TreeNode(6)
tree.root.right.left=TreeNode(8)
tree.root.right.right=TreeNode(11)
res=[]
res=tree.preorder_print(tree.root,res)
print(res)
res=tree.preorderTraversal(tree.root)
print(res)

res=[]
res=tree.inorder_print(tree.root,res)
print(res)
res=tree.inorderTraversal(tree.root)
print(res)

res=[]
#res=tree.postorder_print(tree.root,res)
#print(res)
res=tree.postorderTraversal(tree.root)
print(res)
