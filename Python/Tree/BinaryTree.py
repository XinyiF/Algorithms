class BTree(object):

    # 初始化
    def __init__(self, data=None, left=None, right=None):
        self.data = data    # 数据域
        self.left = left    # 左子树
        self.right = right  # 右子树

    #前序遍历 根左右
    def preorder(self):
        if self.data:
            print(self.data,end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()


    # 中序遍历 左根右
    def inorder(self):
        if self.left:
            self.left.inorder()
        if self.data:
            print(self.data, end=' ')
        if self.right:
            self.right.inorder()


    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        if self.data:
            print(self.data, end=' ')

    # 非递归遍历
    def preorder2(self):
        stack=[]
        output=[]
        while stack or self:
            while self:
                stack.append(self)
                output.append(self.data)
                self=self.left
            temp=stack.pop()
            self=temp.right
        return output

    def inorder2(self):
        stack=[]
        output=[]
        while stack or self:
            while self:
                stack.append(self)
                self=self.left
            temp = stack.pop()
            output.append(temp.data)
            self=temp.right
        return output


    # 先得到根右左，再倒过来
    def postorder2(self):
        stack=[]
        output=[]
        while self or stack:
            while self:
                stack.append(self)
                output.append(self.data)
                self=self.right
            temp=stack.pop()
            self=temp.left
        return output[::-1]

    # 分治算法
    def preorder3(self,node):
        if not node:
            return []
        return [node.data]+self.preorder3(node.left)+self.preorder3(node.right)

    def inorder3(self,node):
        if not node:
            return []
        return self.inorder3(node.left)+[node.data]+self.inorder3(node.right)

    def postorder3(self,node):
        if not node:
            return []
        return self.postorder3(node.left)+self.postorder3(node.right)+[node.data]




    def lowestCommonAncestor(self, root, p, q):
        if root==p or root==q or not root:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,q,p)
        if not left:
            return right
        if not right:
            return left
        return root

    # 队列
    def BFS(self,root):
        queue=[root]
        output=[]
        while queue:
            root=queue[0]
            queue=queue[1:]
            output.append(root.data)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
            if not root:
                break
        return output
















def main():
    # 构造二叉树, BOTTOM-UP METHOD
    right_tree = BTree(6)
    right_tree.left = BTree(2)
    right_tree.right = BTree(4)

    left_tree = BTree(5)
    left_tree.left = BTree(1)
    left_tree.right = BTree(3)

    tree = BTree(11)
    tree.left = left_tree
    tree.right = right_tree

    left_tree = BTree(7)
    left_tree.left = BTree(3)
    left_tree.right = BTree(4)

    right_tree = tree # 增加新的变量
    tree = BTree(18)
    tree.left = left_tree
    tree.right = right_tree

    print(tree.BFS(tree))




if __name__ == "__main__":
    main()