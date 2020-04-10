#Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
class Solution(object):
    def numTrees(self, n):
        if n<1:return 0
        count={}
        count[0],count[1],count[2]=1,1,2
        for i in range(3,n+1): # from n=3 to n=n
            count[i]=0
            for j in range(1,i+1):
                count[i]+=count[j-1]*count[i-j]
        return count[n]

res=Solution()
print(res.numTrees(3))

