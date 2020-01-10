#Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
class Solution(object):
    def combine(self, n, k):
        if n<1 or k<1:return
        res,temp=[],[]
        self.helper(1,k,n,res,temp)
        return res

    def helper(self,start,k,n,res,temp):
        if k==0:res.append(temp[:])
        else:
            for i in range(start,n+1):
                temp.append(i)
                self.helper(i+1,k-1,n,res,temp)
                temp.pop()
n,k=4,3
result=Solution()
print(result.combine(n,k))
