class TreeNode(object):

    # 初始化
    def __init__(self, val=None, left=None, right=None):
        self.val = val    # 数据域
        self.left = left    # 左子树
        self.right = right  # 右子树

    #前序遍历 根左右
    def preorder(self):
        if self.val:
            print(self.val,end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()


    # 中序遍历 左根右
    def inorder(self):
        if self.left:
            self.left.inorder()
        if self.val:
            print(self.val, end=' ')
        if self.right:
            self.right.inorder()


    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        if self.val:
            print(self.val, end=' ')

    # 非递归遍历
    def preorder2(self):
        stack=[]
        output=[]
        while stack or self:
            while self:
                stack.append(self)
                output.append(self.val)
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
            output.append(temp.val)
            self=temp.right
        return output


    # 先得到根右左，再倒过来
    def postorder2(self):
        stack=[]
        output=[]
        while self or stack:
            while self:
                stack.append(self)
                output.append(self.val)
                self=self.right
            temp=stack.pop()
            self=temp.left
        return output[::-1]

    # 分治算法
    def preorder3(self,node):
        if not node:
            return []
        return [node.val]+self.preorder3(node.left)+self.preorder3(node.right)

    def inorder3(self,node):
        if not node:
            return []
        return self.inorder3(node.left)+[node.val]+self.inorder3(node.right)

    def postorder3(self,node):
        if not node:
            return []
        return self.postorder3(node.left)+self.postorder3(node.right)+[node.val]




    def lowestCommonAncestor(self, root, p, q):
        """

        :param root: 根节点
        :param p: 节点p
        :param q: 节点q
        :return: p和q最近的公共祖先
        """
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
            output.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
            if not root:
                break
        return output

    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        start=root
        while root:
            if val<root.val:
                if not root.left:
                    root.left=TreeNode(val)
                    return start
                root= root.left
            else:
                if not root.right:
                    root.right=TreeNode(val)
                    return start
                root=root.right





















def main():
    # 构造二叉树, BOTTOM-UP METHOD
    right_tree = TreeNode(6)
    right_tree.left = TreeNode(2)
    right_tree.right = TreeNode(4)

    left_tree = TreeNode(5)
    left_tree.left = TreeNode(1)
    left_tree.right = TreeNode(3)

    tree = TreeNode(11)
    tree.left = left_tree
    tree.right = right_tree

    left_tree = TreeNode(7)
    left_tree.left = TreeNode(3)
    left_tree.right = TreeNode(4)

    right_tree = tree # 增加新的变量
    tree = TreeNode(18)
    tree.left = left_tree
    tree.right = right_tree

    print(tree.BFS(tree))




if __name__ == "__main__":
    main()