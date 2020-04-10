#Then print out all the strings that can be arranged by the input characters
class Solution:
    def Permutation(self, ss):
        list,stack,res=[],[],[]
        if len(ss)==0:return res
        for i in ss:
            list.append(i)
        self.helper(list,stack,res)
        return res
    def helper(self, list, stack,res):
        if not list:
            temp=''
            for i in stack:
                temp+=i
            if temp not in res:
                res.append(temp)
        else:
            for i in range(len(list)):
                stack.append(list[i])
                del list[i]
                self.helper(list, stack,res)
                list.insert(i, stack.pop())









s='122'
res=Solution()
res.Permutation(s)





