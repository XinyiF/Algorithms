#mock the function min, top...based on 2 stacks
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        self.stack1.append(node)
        if not self.stack2:
            self.stack2.append(node)
        else:
            if self.stack2[-1]<node:
                self.stack2.append(self.stack2[-1])
            else:
                self.stack2.append(node)
    def pop(self):
        if self.stack1:
            self.stack2.pop()
            return self.stack1.pop()
    def top(self):
        return self.stack1[-1]
    def min(self):
        return self.stack2[-1]


res=Solution()
print(res.push(3))
print(res.push(2))
print(res.min())
print(res.top())
