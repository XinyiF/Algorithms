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

    out=tree.preorder2()
    print(out)
    tree.preorder()
    print('')

    out=tree.inorder2()
    print(out)
    tree.inorder()
    print('')

    out=tree.postorder2()
    print(out)
    tree.postorder()
    print('')

if __name__ == "__main__":
    main()